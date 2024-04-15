/// <reference types="@angular/localize" />

import { Component } from '@angular/core';
import { bootstrapApplication } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import 'zone.js';
import { appConfig } from './app/app.config';

@Component({
  selector: 'app-root',
  standalone: true,
  template: `
  <div>
    <h2>Enter details:</h2>
    <router-outlet></router-outlet>
  </div>
    
  `,
  imports: [RouterModule],
})
export class App {
  name = 'Angular';
}

bootstrapApplication(App, appConfig);
