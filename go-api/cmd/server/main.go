package main

import (
	"fmt"
	"log"
	"net/http"

	"github.com/Minke-Crafford/sandbox/go-api/internal/handlers"
)

func main() {
	// Create a new HTTP server mux
	mux := http.NewServeMux()

	// Register routes
	mux.HandleFunc("/", handlers.HomeHandler)
	mux.HandleFunc("/health", handlers.HealthHandler)
	mux.HandleFunc("/api/hello", handlers.HelloHandler)

	// Server configuration
	port := ":8080"
	fmt.Printf("Starting server on port %s...\n", port)

	// Start the server
	if err := http.ListenAndServe(port, mux); err != nil {
		log.Fatalf("Failed to start server: %v", err)
	}
}
