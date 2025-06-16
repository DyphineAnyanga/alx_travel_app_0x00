// interfaces/index.ts

export interface Movie {
  id: string;
  titleText: {
    text: string;
  };
  releaseYear: {
    year: number;
  };
  primaryImage?: {
    url: string;
  };
}

export interface MoviesResponse {
  page: number;
  results: Movie[];
}
