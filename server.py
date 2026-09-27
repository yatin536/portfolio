"""
Zero-Dependency Python Web Server for Yatin Kumar Singh's Portfolio.
Uses Python's built-in http.server module (no pip install needed).

Usage:
    python server.py [port]
"""

import http.server
import socketserver
import os
import sys

def run_server(port=8000):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dist_dir = os.path.join(base_dir, 'dist')

    # If dist doesn't exist yet, run build_static
    if not os.path.exists(os.path.join(dist_dir, 'index.html')):
        print("dist/ not found. Running static site builder...")
        try:
            from build_static import build
            build()
        except Exception as e:
            print(f"Build failed: {e}")

    serve_dir = dist_dir if os.path.exists(dist_dir) else base_dir
    os.chdir(serve_dir)

    handler = http.server.SimpleHTTPRequestHandler

    print("\n" + "=" * 55)
    print(">> Yatin Kumar Singh's Portfolio (Built-in Python Server)")
    print(f">> Serving at: http://localhost:{port}")
    print(f">> Directory:  {serve_dir}")
    print(">> Press Ctrl+C to stop the server")
    print("=" * 55 + "\n")

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", port), handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped gracefully.")

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    run_server(port)
