import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class APIService {
  private http = inject(HttpClient);
  postApiData(formData: any) {
    const headers = { 'content-type': 'application/json' };
    return this.http.post('http://127.0.0.1:5000/get-itinerary', { body: formData }, { headers: headers });
  }
}
