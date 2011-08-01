package org.kod.baskara;

import org.kod.baskara.interfaces.Converte;
import org.kod.baskara.until.Baskara;

public class Main {
	
	private static void imprime(Converte converte) {
		
		System.out.println("A: " + converte.getA() + 
						   "   B: " + converte.getB() +
						   "   C: " + converte.getC() +
						   "   Δ: " + converte.getDelta() +
						   "\n" + converte.resultValues());
		
	}
	
	public static void main(String[] args) {
		
		Baskara baskara = new Baskara();
		imprime(baskara.criar(-1.0, 0.0, 10.0));

	}
	
}