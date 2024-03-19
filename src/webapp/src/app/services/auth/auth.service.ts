import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(
    private http: HttpClient
  ) {
  }

  login(email: string, password: string) : Observable<any> {
    console.log(email, password);
    const url = 'http://localhost:8000/login/'
    const data = { email: email, password: password };
    const httpOptions = {
      headers: { 'Content-Type': 'application/json' }
    };

    return this.http.post(url, JSON.stringify(data), httpOptions)
      
  }
}
