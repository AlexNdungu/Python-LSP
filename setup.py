import subprocess
import json

# Path to pylsp executable
PYLSP_PATH = "./LangSP/Scripts/pylsp.exe"

# Capabilities of the client
CAPABILITIES = {
    "textDocument": {
        "completion": {
            "completionItem": {
                "snippetSupport": True
            }
        }
    }
}

# Counter for request IDs
REQUEST_ID = 0

# Start the language server as a subprocess and use its stdin and stdout as communication channel
lsp = subprocess.Popen([PYLSP_PATH], stdin=subprocess.PIPE, stdout=subprocess.PIPE)


def send_request(method, params):
    """Send a JSON-RPC request to the language server and return the response."""
    global REQUEST_ID
    # Increment the request ID
    REQUEST_ID += 1
    # Construct the request message
    request = {
        "jsonrpc": "2.0",
        "id": REQUEST_ID,
        "method": method,
        "params": params
    }
    # Encode the request as JSON
    request_json = json.dumps(request)
    # Write the request to the language server's stdin
    lsp.stdin.write(request_json.encode())
    lsp.stdin.write(b'\n')
    lsp.stdin.flush()
    # Read the response from the language server's stdout
    response_json = lsp.stdout.readline()
    # Decode the response as JSON
    response = json.loads(response_json)
    # Return the response
    return response

def send_notification(method, params):
    """Send a JSON-RPC notification to the language server."""
    # Construct the notification message
    notification = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params
    }
    # Encode the notification as JSON
    notification_json = json.dumps(notification)
    # Write the notification to the language server's stdin
    lsp.stdin.write(notification_json.encode())
    lsp.stdin.write(b'\n')
    lsp.stdin.flush()

def read_message():
    """Read a JSON-RPC message from the language server and return it."""
    # Read a message from the language server's stdout
    message_json = lsp.stdout.readline()
    # Decode the message as JSON
    message = json.loads(message_json)
    # Return the message
    return message
