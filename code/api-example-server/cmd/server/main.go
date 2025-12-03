package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
	// Create a Gin router with default middleware (logger and recovery)
	r := gin.Default()

	// Define a simple GET endpoint
	r.GET("/hello", func(c *gin.Context) {
		// Return JSON response
		c.JSON(http.StatusOK, gin.H{
			"message": "Hello, there",
		})
	})

	r.PUT("/hello", func(c *gin.Context) {

		buf := []byte{}
		c.Request.Body.Read(buf)
		msg := map[string]string{}
		json.Unmarshal(buf, &msg)

		if name, ok := msg["name"]; ok {

			// Return JSON response
			c.JSON(http.StatusOK, gin.H{
				"message": fmt.Sprintf("Hello, %s", name),
			})
			return
		}
		// Return JSON response
		c.JSON(http.StatusOK, gin.H{
			"message": "Hello, there",
		})
	})

	// Start server on port 8080 (default)
	// Server will listen on 0.0.0.0:8080 (localhost:8080 on Windows)
	if err := r.Run(); err != nil {
		log.Fatalf("failed to run server: %v", err)
	}
}
