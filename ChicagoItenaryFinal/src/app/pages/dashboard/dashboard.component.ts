import { Component, OnInit } from '@angular/core';
import {
  FormBuilder,
  ReactiveFormsModule,
  UntypedFormGroup,
} from '@angular/forms';
import {
  NgbAlertModule,
  NgbDatepickerModule,
  NgbDateStruct,
} from '@ng-bootstrap/ng-bootstrap';
import { APIService } from '../../services/api.service';
import { HttpClientModule } from '@angular/common/http';
import { firstValueFrom, fromEvent } from 'rxjs';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [ReactiveFormsModule, NgbDatepickerModule, HttpClientModule],
  providers: [APIService],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css',
})
export class DashboardComponent implements OnInit {
  travelForm!: UntypedFormGroup;
  outputText = '';
  outputMap = '';
  constructor(private fb: FormBuilder, private apiService: APIService) {}
  ngOnInit() {
    this.travelForm = this.fb.group({
      from: [''],
      typeOfPlace: [''],
      numberOfPlaces: [0],
      date: [new Date()],
    });
  }

  async handleSubmit() {
    console.log(this.travelForm?.value);
    try {
      const { text, map } = (await firstValueFrom(
        this.apiService.postApiData(this.travelForm.value)
      )) as any;
      this.outputText = text;
      this.outputMap = map;
    } catch (err) {
      console.log(err);
    }
  }
}
