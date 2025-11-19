package utils

import (
	"fmt"
	"time"
)

// GetTimestamp returns the current timestamp as a string
func GetTimestamp() string {
	return time.Now().Format(time.RFC3339)
}

// FormatMessage formats a message with a timestamp
func FormatMessage(msg string) string {
	return fmt.Sprintf("[%s] %s", GetTimestamp(), msg)
}
