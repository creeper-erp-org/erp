import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormControl, FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app.routes';

  

@NgModule({
  declarations: [AppComponent, LoginComponent],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    FormsModule,
    NgModule,
    FormControl,
    BrowserModule,
    AppRoutingModule
  ]
})


export class AppModule { }
