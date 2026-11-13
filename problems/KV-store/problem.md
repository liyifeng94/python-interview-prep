# DESCRIPTION

Implement a key-value store that can serialize multiple string key-value pairs into a single string and deserialize it back. Both keys and values can contain any characters including delimiters, newlines, and special characters. For example, serializing `{"key:1": "val=ue", "k\ney": "v"}` should produce a string that can be deserialized back to the exact same dictionary.

## Input:
```
{"name": "John:Doe", "city": "New,York"}
```
## Output:
```
Serialize(dict): "Serialized string" 
Deserialize("Serialized string"): original dict
```

Explanation: Serialization is the process of converting a dictionary into a string, and deserialization is the process of converting a string back into a dictionary.

Constraints:

- Keys and values are strings that can contain any character (including delimiters, newlines, quotes)
- Serialization must be reversible - deserialize(serialize(data)) == data
- Must handle empty strings and empty dictionaries


# Follow Up

# Chunked Serialization with Metadata Tracking

The core challenge shifts from serializing the entire KV store as one blob to splitting it into fixed-size chunks (e.g., 1KB each) for upload or storage. This matters because real systems often have size constraints on network packets, API payloads, or storage blocks. You'll need a way to track how many chunks exist so deserialization knows when to stop reading.

The key insight is introducing a metadata file that stores critical information like total_chunks count before writing the actual data chunks. During serialization, you write the metadata first, then split your serialized KV data into 1KB chunks as separate files or blocks. During deserialization, you read the metadata to know exactly how many chunks to fetch and reassemble.

Important considerations include:

Handling the last chunk which will likely be smaller than 1KB
Deciding whether to split on byte boundaries (simple) or respect character boundaries to avoid corrupting multi-byte UTF-8 sequences
Choosing a naming scheme for chunk files (e.g., data_chunk_0, data_chunk_1) that preserves order
Ensuring atomic writes of metadata so you never have orphaned chunks