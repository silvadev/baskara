package org.kod.baskara;

import org.kod.baskara.interfaces.Converte;
import org.kod.baskara.until.Baskara;

public class Main {
	
	private static void imprime(Converte converte) {
		/*
		 * Este método imprime no formato da função todos os 
		 * dados possíveis.
		 */
		System.out.println("a: " + converte.getA() + 
						   "   b: " + converte.getB() +
						   "   c: " + converte.getC() +
						   "   Δ: " + converte.getDelta() +
						   "\n" + converte.resultValues() + "\n");
		
	}
	
	public static void main(String[] args) {
		//TODO Criar método de entrada dinâmica para evitar recompilar código.
		Baskara baskara = new Baskara();
		imprime(baskara.criar("1" , "", "2"));
		imprime(baskara.criar("1", "5", ""));
		imprime(baskara.criar("", "", ""));
		imprime(baskara.criar("-2", "10", "200"));

	}
	
}