package org.kod.baskara.until;

import org.kod.baskara.interfaces.Converte;
import org.python.core.PyObject;
import org.python.core.PyFloat;
import org.python.util.PythonInterpreter;


public class Baskara {
	public static PyObject baskaraClass;
	
	public Baskara() {
		PythonInterpreter interpretador = new PythonInterpreter();
		interpretador.exec("from Baskara import Baskara");
		baskaraClass = interpretador.get("Baskara");
		
	}
	
	public Converte criar (Double avalue, Double bvalue, Double cvalue) {
		
		PyObject baskaraObject = baskaraClass.__call__(new PyFloat(avalue), 
													   new PyFloat(bvalue), 
													   new PyFloat(cvalue));
		return (Converte)baskaraObject.__tojava__(Converte.class);
		
	}
	
}
