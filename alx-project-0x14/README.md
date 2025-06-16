# CineSeek - MoviesDatabase API Integration

This project demonstrates how to consume the [MoviesDatabase API](https://moviesdatabase.p.rapidapi.com) using Next.js, TypeScript, and Tailwind CSS. It includes real-time movie search, filtering by year and genre, and viewing detailed movie information.

## API Overview

The MoviesDatabase API provides extensive movie and TV show data, including:
- Titles, genres, and release years
- Ratings and popularity
- Images and descriptions
- Advanced search capabilities
- Pagination support

This API is ideal for building applications that require access to movie databases or entertainment metadata.

## Version

Current Version: **v1.0**

## Available Endpoints

| Endpoint | Description |
|----------|-------------|
| `/titles` | Returns a list of movies and TV titles. Supports filters like `year`, `genre`, and pagination. |
| `/titles/{id}` | Fetches details for a specific movie or TV title by ID. |
| `/titles/search/title/{name}` | Searches for titles by name. |
| `/genres` | Returns available movie genres. |
| `/years` | Lists all available release years. |

## Request and Response Format

### Sample Request

```http
GET /titles?page=1&genre=action&year=2020
Host: moviesdatabase.p.rapidapi.com
x-rapidapi-key: YOUR_API_KEY
x-rapidapi-host: moviesdatabase.p.rapidapi.com
