package main

import (
	"fmt"
	"log"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/google/uuid"
)

var messages = map[string]string{}

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

	r.GET("/hello/:id", func(c *gin.Context) {

		if name, ok := messages[c.Param("id")]; ok {
			// Return JSON response
			c.JSON(http.StatusOK, gin.H{
				"message": fmt.Sprintf("Hello, %s", name),
			})
			return
		}
		// Return JSON response
		c.JSON(http.StatusNotFound, gin.H{
			"error": "id is not ready yet...",
		})
		return
	})

	r.POST("/hello", func(c *gin.Context) {

		msg := map[string]string{}
		if err := c.ShouldBindBodyWithJSON(&msg); err != nil {
			c.AbortWithError(500, err)
			return
		}

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

	r.POST("/delayed-hello", func(c *gin.Context) {
		id := uuid.NewString()

		msg := map[string]string{}
		if err := c.ShouldBindBodyWithJSON(&msg); err != nil {
			c.AbortWithError(500, err)
			return
		}

		if name, ok := msg["name"]; ok {

			// make a go routine that delayes hello being ready
			go func() {
				<-time.After(10 * time.Second)
				messages[id] = name
			}()

			// Return JSON response
			c.JSON(http.StatusOK, gin.H{
				"id": id,
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
