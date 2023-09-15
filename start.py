from setup import send_request, send_notification, CAPABILITIES
import os

print("Starting language server...")

# Send an initialize request with rootUri, capabilities, and initializationOptions

# Get the current directory
current_dir = os.path.dirname(os.path.realpath(__file__))

print("Current directory: " + current_dir)

initialize_params = {
    "rootUri": "file://C:/Users/Alex Meta Ndung'u/Documents/Py Projects/LSP",
    "capabilities": CAPABILITIES,
    "initializationOptions": {}
}

initialize_response = send_request("initialize", initialize_params)
print(initialize_response)

# # Send an initialized notification with no parameters
# send_notification("initialized", {})

# # Send a textDocument/didOpen notification with document URI, language ID, version number, and text content
# did_open_params = {
#   "textDocument": {
#       "uri": "file:///path/to/your/file.py",
#       "languageId": "python",
#       "version": 1,
#       "text": "# Your Python code here"
#   }
# }
# send_notification("textDocument/didOpen", did_open_params)

# # Send a textDocument/completion request with document URI and position of cursor
# completion_params = {
#   "textDocument": {
#       "uri": "file:///path/to/your/file.py"
#   },
#   "position": {
#       "line": 0,
#       "character": 1
#   }
# }

# completion_response = send_request("textDocument/completion", completion_params)
# print(completion_response)
