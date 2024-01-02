/** @odoo-module **/

import { registry } from "@web/core/registry"
const { markup } = owl

export const basicService ={
    start(){
          function normalFunction(){
          return "this is a normal Function"}

          const arrowFunction = ()=>{
          return "this is an arrow Function"}
     return{
        string:"Basic Services",
        boolean:"true",
        integer:"1",

        float:"0.5",
        array:[1,2,3],
        object:{"key": "value"},

        "function":()=>{
        console.log("This IS FUNCTION has been called")
        return "Service function has been called."},
        normal_function: normalFunction(),
        arrow_function: arrowFunction(),
        html:markup("<button class='btn btn-primary' onclick='alert(1111111111)'>Button</button>"),



        }
        }
}
registry.category("services").add("basicService",basicService)