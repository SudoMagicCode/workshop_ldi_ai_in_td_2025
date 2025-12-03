# Stage 1: The Build Stage
FROM golang:1.25-alpine AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy go.mod and go.sum first to leverage Docker's build cache
# This means dependencies won't be re-downloaded unless go.mod/go.sum changes
COPY go.mod go.sum ./

# Download all the dependencies
RUN go mod download

# Copy the rest of the source code
COPY . .

# Build the Go application
# -o main: specifies the output file name as 'main'
# -ldflags -s -w: reduces the binary size by omitting debugging information
# ./cmd/server: specifies the path to the main package (adjust this path as needed)
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o main ./cmd/server

# ---

# Stage 2: The Final (Minimal) Stage
# Use a minimal base image like scratch for the smallest possible final image
# Scratch images contain virtually nothing, only the compiled binary is needed.
FROM scratch

# Copy the built binary from the 'builder' stage
COPY --from=builder /app/main /usr/local/bin/server

# Expose the port your application listens on
EXPOSE 8080

# Define the command to run the executable
ENTRYPOINT ["/usr/local/bin/server"]