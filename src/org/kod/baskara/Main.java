package org.kod.baskara;

import org.kod.baskara.interfaces.Converte;
import org.kod.baskara.until.Baskara;

public class Main {
	
	private static void imprime(Converte converte) {
		
		System.out.println("a: " + converte.getA() + 
						   "   b: " + converte.getB() +
						   "   c: " + converte.getC() +
						   "   Δ: " + converte.getDelta() +
						   "\n" + converte.resultValues());
		
	}
	
	public static void main(String[] args) {
		
		Baskara baskara = new Baskara();
		imprime(baskara.criar("" , "-5", "193"));

	}
	
}