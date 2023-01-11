versoin: '3'

services:
  backend-api:
    image: 'backend-api:latest'
    environment:
      - 'APP_PORT=8080'
      - 'APP_HOST=dev'
    ports:
      - '8080:8080'
    volumes:
      - './backend-api:/app'

  backend-dataretrieval:
    image: 'backend-dataretrieval:latest'
    environment:
      - 'APP_PORT=8081'
      - 'APP_HOST=dev'
    ports:
      - '8081:8081'
    volumes:
      - './backend-dataretrieval:/app'
  
  backend-monitoring:
    image: 'backend-monitoring:latest'
    environment:
      - 'APP_PORT=8082'
      - 'APP_HOST=dev'
    ports:
      - '8082:8082'
    volumes:
      - './backend-monitoring:/app'

  backend-predictions:
    image: 'backend-predictions:latest'
    environment:
      - 'APP_PORT=8083'
      - 'APP_HOST=dev'
    ports:
      - '8083:8083'
    volumes:
      - './backend-predictions:/app'
    
  frontend:
    image: 'frontend:latest'
    environment:
      - 'APP_PORT=8080'
      - 'APP_HOST=dev'
    ports:
      - '8080:8080'
    volumes:
      - './frontend:/app'