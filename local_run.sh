#!/bin/bash

WATCH_MODE=false

# Parse arguments
for arg in "$@"; do
	case $arg in
	--watch)
		WATCH_MODE=true
		shift
		;;
	esac
done

echo "Installing dependencies with Poetry..."
poetry install --no-root

if [ "$WATCH_MODE" = true ]; then
	echo "Starting in watch mode..."

	# Start server in background
	poetry run python -m http.server --directory dist 8000 &
	SERVER_PID=$!

	# Watch for changes and rerun generator
	poetry run watchmedo shell-command \
		--patterns="*.py;*.txt;*.md;*.json" \
		--recursive \
		--command='echo "Changes detected, regenerating..."; poetry run python script.py'

	# Kill the server when watchmedo stops
	kill $SERVER_PID
else
	echo "Running generator script..."
	poetry run python script.py

	echo "Serving at http://localhost:8000"
	python -m http.server --directory dist 8000
fi
