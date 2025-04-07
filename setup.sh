#!/bin/bash

# Create .venv using uv if it doesn't exist
if [ ! -d ".venv" ]; then
  echo "🔧 Creating virtual environment with uv..."
  uv venv
  echo "✅ .venv created"
fi

# Install dependencies with uv
echo "📦 Installing dependencies..."
uv pip install -r requirements.txt

# Create Configurations folder
if [ ! -d "Configurations" ]; then
  mkdir -p Configurations
  echo "✅ Created Configurations/ folder"
fi

# Create config.ini inside Configurations
if [ ! -f "Configurations/config.ini" ]; then
  cat <<EOL > Configurations/config.ini

EOL
  echo "✅ Created Configurations/config.ini"
fi

# Create Logs folder inside Configurations
if [ ! -d "Configurations/Logs" ]; then
  mkdir -p Configurations/Logs
  echo "✅ Created Configurations/Logs/ folder"
fi

# Create logs.log inside Logs
if [ ! -f "Configurations/Logs/logs.log" ]; then
  touch Configurations/Logs/logs.log
  echo "✅ Created Configurations/Logs/logs.log"
fi

# Create .env file if missing
if [ ! -f ".env" ]; then
  touch .env
  echo "# Add your environment variables here" > .env
  echo "✅ Created .env file"
fi

echo "🎉 Setup complete!"
