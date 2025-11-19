package handlers

import (
	"encoding/json"
	"net/http"
)

// Response represents a standard API response
type Response struct {
	Message string `json:"message"`
	Status  string `json:"status"`
}

// HomeHandler handles the root endpoint
func HomeHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(Response{
		Message: "Welcome to the Go API",
		Status:  "success",
	})
}

// HealthHandler handles the health check endpoint
func HealthHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(Response{
		Message: "Service is healthy",
		Status:  "ok",
	})
}

// HelloHandler handles the hello endpoint
func HelloHandler(w http.ResponseWriter, r *http.Request) {
	name := r.URL.Query().Get("name")
	if name == "" {
		name = "World"
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(Response{
		Message: "Hello, " + name + "!",
		Status:  "success",
	})
}
