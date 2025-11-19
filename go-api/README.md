# Go API Project

A simple REST API server built with Go's standard library.

## Structure

```
go-api/
├── cmd/
│   └── server/          # Application entry points
│       └── main.go      # Main server application
├── internal/
│   └── handlers/        # HTTP request handlers
│       └── handlers.go
├── pkg/
│   └── utils/          # Shared utilities
│       └── utils.go
└── go.mod              # Go module definition
```

## Getting Started

### Prerequisites

- Go 1.21 or higher

### Running the Server

```bash
cd go-api
go run cmd/server/main.go
```

The server will start on `http://localhost:8080`

### Available Endpoints

- `GET /` - Root endpoint with welcome message
- `GET /health` - Health check endpoint
- `GET /api/hello?name=YourName` - Hello endpoint with optional name parameter

### Building

```bash
go build -o bin/server cmd/server/main.go
```

### Testing

```bash
go test ./...
```

## Development

This is a skeleton project. Add your own routes, handlers, and business logic as needed.
