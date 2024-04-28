// el ciclo nos permite ejecutar un codigo las veces que queramos 
/* 

// while (mientras)

let contador = 0; // este es el contador

while (contador < 10){
    console.log("Hola mundo" + contador);
    contador = contador + 1;
}

// do while la dif es el roden como se ejecutan las cosas la primera vez

let z = 5;
do {
  console.log("Ciclo do...while número " + z);
     z++;
} while (z < 5);

//for (contador, condicion, incrementador)

for (let x = 0; x < 10; x++) {
    console.log("Ciclo número " + x);
}

// for anidado: se ejecuta 1 condicion y dentro de la misma, el otro for que cree

for (let x = 0; x < 10; x++) {
 console.log("Ciclo número " + x);

  for (let y = 0; y < 5; y++) {
    console.log("Ciclo secundario " + y);
   }
} 

// switch

let diaDeLaSemana = Number(prompt("Ingrese día de la semana con números")); //se pone el number para pasar de string a numero
switch (diaDeLaSemana) {
     case 1:
         alert("Lunes");
         break; // si no pongo el break se sigue ejecutando todo
     case 2:
         alert("Martes");
         break;
     case 3:
         alert("Miércoles");
         break;
     case 4:
         alert("Jueves");
         break;
     case 5:
         alert("Viernes");
         break;
     case 6:
         alert("Sábado");
         break;
     case 7:
         alert("Domingo");
         break;
     default:
         alert("Ese día no existe");
         break;
 }

*/