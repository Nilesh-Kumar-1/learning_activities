import { Component, OnInit } from '@angular/core';

@Component({
  // selector: '[app-servers]',
  selector: 'app-servers',
  // selector: '.app-servers',
  
  // template:`
  // <h2>Servers</h2>
  // <p>Servers is working !</p>
  // `,
  templateUrl: './servers.component.html',
  // styleUrl: './servers.component.css'
  styles:`h2{color:red}`
})
export class ServersComponent implements OnInit{

  allownewserver=false
  serverCreationStatus= 'No servers created yet...';
  serverName=""
  ngOnInit() {
    
  }

  constructor(){
    setTimeout(()=> this.allownewserver = true ,1000)
  }

  OnCreateServer(){
    this.serverCreationStatus="Server was created ..."

  }
  onUpdateSevername($event: any) {
    console.log(event)
    this.serverName=$event.target.value;
    throw new Error('Method not implemented.');
    }

}
