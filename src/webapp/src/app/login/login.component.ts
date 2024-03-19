import { Component } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { AuthService } from '../services/auth/auth.service';
import { Observable, catchError, of, throwError } from 'rxjs';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  

styleUrl: './login.component.css'
})


export class LoginComponent {
  title = 'login-page'
  loginForm: FormGroup;
  data: any;
  errorMessage: string;
  constructor(private fb: FormBuilder,
    private authService: AuthService
    ) {
    this.loginForm = this.fb.group({
      username: ['', Validators.required],
      password: ['', Validators.required],
    });
  }

  login() {
    
    console.log(this.loginForm.value.username);
    this.authService.login(this.loginForm.value.username, this.loginForm.value.password).pipe(
      catchError((error: any) => {
        // Handle the error here in a user-friendly way
        console.log('Login error:', error);  // Log for debugging
    
        // Display an error message to the user (consider using a toast or modal)
        // this.errorMessage = 'An error occurred during login. Please try again.';
    
        // Optionally, retry the login or redirect to a login error page
        // return throwError(error);  // For retry logic (uncomment if needed)
        // return of({ redirectTo: '/login-error' });  // For redirect (uncomment if needed)
        
        return of(error);  // Re-throw by default for propagating the error
      })
    ).subscribe(response => {
      this.data = response;
      console.log(this.data);
    });
  }
}