# Development Stage
FROM node:18-alpine AS development

WORKDIR /app

# Install dependencies first (caching)
COPY package*.json ./
RUN npm ci --force

# Copy rest of the application
COPY . .

# Expose port
EXPOSE 3000

# Start development server
CMD ["npm", "run", "dev"]

# Production Stage
FROM node:18-alpine AS production

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm ci --force

#Modify at the later stage
#RUN npm ci --only=production
RUN npm ci 
# Copy source
COPY . .

# Build application
RUN npm run build

# Expose port
EXPOSE 3000

# Start production server
CMD ["npm", "start"]