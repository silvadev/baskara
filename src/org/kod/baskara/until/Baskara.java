/*
 * Esta classe intermedia entre a classe Baskara.py e o aplicativo Java. 
 */
package org.kod.baskara.until;

import org.kod.baskara.interfaces.Converte;
import org.python.core.PyObject;
import org.python.core.PyString;
import org.python.util.PythonInterpreter;


public class Baskara {
	public static PyObject baskaraClass;
	
	public Baskara() {
		/*
		 * Este método chama a classe Baskara em Baskara.py
		 * e o coloca na variável baskaraClass.
		 */
		PythonInterpreter interpretador = new PythonInterpreter();
		interpretador.exec("from Baskara import Baskara");
		baskaraClass = interpretador.get("Baskara");
		
	}
	
	public Converte criar (String avalue, String bvalue, String cvalue) {
		/*
		 * Este método cria uma instância para a classe baskaraClass passando
		 * os valores de 'a', 'b' e 'c' para o __init__ de Baskara.py
		 * e transforma o retorno das funções em tipos padrões da linguagem Java.
		 */
		PyObject baskaraObject = baskaraClass.__call__(new PyString(avalue), 
													   new PyString(bvalue), 
													   new PyString(cvalue));
		return (Converte)baskaraObject.__tojava__(Converte.class);
		
	}
	
}
