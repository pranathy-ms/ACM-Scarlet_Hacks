import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class APIService {
  private http = inject(HttpClient);
  postApiData(formData: any): Observable<any> {
    const headers = { 'content-type': 'application/json' };
    const reqData = {
      starting_location: formData.from,
      number_of_places: formData.numberOfPlaces,
      start_date_time: formData.date,
      types_of_places: formData.typeOfPlace,
    };
    return this.http.post('http://127.0.0.1:5000/get-itinerary', reqData, {
      headers: headers,
    });
  }
}
