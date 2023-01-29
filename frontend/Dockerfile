# Use a Node.js base image
FROM node:14

# Set the working directory
WORKDIR /app

# Copy the package.json file to the container
COPY package.json .

# Install the dependencies
RUN pnpm install

# Copy the rest of the code to the container
COPY . .

# Build the frontend
RUN pnpm run build

# Set the command to run when the container starts
CMD [ "pnpm", "start" ]
