var initX = 300;
var initY = 300;
var raio = 400;


void setup()
{
	size(600, 600);
	//cor roxa
	strokeWeight(8);
	stroke(199, 122, 246);
	// largura da linha
  
}

void draw() 
{
  
	background(0);
	//Bola Branca do Fundo
	ellipse(initX, initY, raio, raio);

  
  // MICRO MARCAS
	var aux = 0;
	for(aux=0; aux<60 ; aux++)
	{

		var auxPi = map(aux, 0, 60, 0, TWO_PI) - HALF_PI

		// Ponteiro Hora 
		if(aux %15 == 0)
		{
			stroke(254, 215, 102);
			strokeWeight(6);

			line(cos(auxPi) * (raio/20*7) + initX,  sin(auxPi) * (raio/20*7) + initY,  cos(auxPi) * (raio/2) + initX, sin(auxPi) * (raio/2) + initY);
		}
		else if(aux % 5 == 0)
		{
			strokeWeight(3);

			line(cos(auxPi) * (raio/20*8) + initX,  sin(auxPi) * (raio/20*8) + initY,  cos(auxPi) * (raio/2) + initX, sin(auxPi) * (raio/2) + initY);
		}
		else
		{
			strokeWeight(1);

			line(cos(auxPi) * (raio/20*9) + initX,  sin(auxPi) * (raio/20*9) + initY,  cos(auxPi) * (raio/2) + initX, sin(auxPi) * (raio/2) + initY);
		}

	}


	// Calculo horario
	var segundo = map(second(), 0, 60, 0, TWO_PI) - HALF_PI;


	var minuto = map(minute(), 0, 60, 0, TWO_PI) + map(segundo + HALF_PI, 0, TWO_PI, 0, TWO_PI/60) - HALF_PI;

	var hora = map(hour() % 12, 0, 12, 0, TWO_PI) + map(minuto + HALF_PI, 0, TWO_PI, 0, TWO_PI/12) - HALF_PI;


	//ponteiro segundo
	stroke(254, 74, 73);
	strokeWeight(2);

	line(initX, initY,  cos(segundo) * (raio/20*9) + initX, sin(segundo) * (raio/20*9) + initY);

	//ponteiro minuto
	stroke(204, 102, 0);
	strokeWeight(4);
	line(initX, initY, cos(minuto) * (raio/8*3) + initX, sin(minuto) * (raio/8*3) + initY,);


	//ponteiro hora
	stroke(42, 183, 202);
	strokeWeight(6);
	line(initX, initY, cos(hora) * (raio/4) + initX, sin(hora) * (raio/4) + initY);

  
}