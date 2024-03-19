import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(
    private http: HttpClient
  ) {
  }

  login(email: string, password: string) {
    console.log(email, password);
    const url = 'https://laughing-engine-7pvp5q4jgqvhx6v4-8000.app.github.dev/login/'
    const data = { email: email, password: password };

    this.http.post(url, data)
      .subscribe((response: any) => {
        console.log('POST request successful!', response);
      }, (error: any) => {
        console.error('Error sending POST request!', error);
      });

  }
}
