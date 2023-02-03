import { Component, OnInit, HostListener } from '@angular/core';
import { QuestionService } from '../service/question.service';
import { interval } from 'rxjs';

@Component({
  selector: 'app-question',
  templateUrl: './question.component.html',
  styleUrls: ['./question.component.scss']
})
export class QuestionComponent {
  public name: string="";
  public questionList:any=[];
  public currentQuestion:number=0;
  public points:number=0;
  counter=60;
  correctAnswer:number=0;
  incorrectAnswer:number=0;
  interval$:any;
  progress:string="0";
  isQuizCompleted:Boolean=false;


  constructor(private questionService : QuestionService){}

  ngOnInit(): void {
    this.name=localStorage.getItem("name")!;
    this.getAllQuestions();
    this.startCounter();
  }

getAllQuestions(){
this.questionService.getQuestionJson()
.subscribe(res=>{
this.questionList=res.questions;
})
}

nextQuestion(){
this.currentQuestion++;
}

previousQuestion(){
this.currentQuestion--;
}

answer(currentQno:number,option:any){
  if(currentQno===this.questionList.length){
    this.isQuizCompleted=true;
    this.stopCounter();
  }
  if(option.correct){
    this.points+=1;
    this.correctAnswer++;
    this.currentQuestion++;
    this.getProgress();
  }else{
    this.currentQuestion++;
    this.incorrectAnswer++;
    this.getProgress();
    this.points-=0.25;

  }
}

startCounter(){
  this.interval$= interval(1000)
  .subscribe(val=>{
    this.counter--;
    if(this.counter===0){
      this.currentQuestion++;
      this.counter=60;
      this.points-=0.25;
    }
  });
  setTimeout(()=>{
    this.interval$.unsubscribe()
  },600000);
}

stopCounter(){
  this.interval$.unsubscribe();
  this.counter=0;
}

resetCounter(){
  this.stopCounter();
  this.counter=60;
  this.startCounter();
}

getProgress(){
  this.progress=((this.currentQuestion/this.questionList.length)*100).toString();
  return this.progress;
}

}
