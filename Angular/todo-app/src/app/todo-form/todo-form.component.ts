import { Component, EventEmitter, Input, Output, SimpleChanges } from '@angular/core';
import { Todo } from '../models/todo';

@Component({
  selector: 'app-todo-form',
  templateUrl: './todo-form.component.html',
  styleUrls: ['./todo-form.component.css']
})
export class TodoFormComponent {
  @Input() selectedTodo: Todo | null = null;
  @Output() addTodo = new EventEmitter<Todo>();
  @Output() editTodo = new EventEmitter<Todo>();

  todo: Todo = {
    id: 0,
    imageUrl: '',
    name: '',
    description: '',
    date: ''
  };

  onSubmit() {
    if (this.selectedTodo) {
      this.editTodo.emit(this.todo);
      this.selectedTodo = null;
    } else {
      this.addTodo.emit(this.todo);
    }
    this.resetForm();
  }

  private resetForm() {
    this.todo = {
      id: 0,
      imageUrl: '',
      name: '',
      description: '',
      date: ''
    };
  }

  ngOnChanges(changes: SimpleChanges) {
    if (changes['selectedTodo'] && changes['selectedTodo'].currentValue) {
      this.todo = { ...(changes['selectedTodo'].currentValue as Todo) };
    }
  }
}
