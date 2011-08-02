package org.kod.baskara.until;

import org.kod.baskara.interfaces.Converte;
import org.python.core.PyObject;
import org.python.core.PyString;
import org.python.util.PythonInterpreter;


public class Baskara {
	public static PyObject baskaraClass;
	
	public Baskara() {
		PythonInterpreter interpretador = new PythonInterpreter();
		interpretador.exec("from Baskara import Baskara");
		baskaraClass = interpretador.get("Baskara");
		
	}
	
	public Converte criar (String avalue, String bvalue, String cvalue) {
		
		PyObject baskaraObject = baskaraClass.__call__(new PyString(avalue), 
													   new PyString(bvalue), 
													   new PyString(cvalue));
		return (Converte)baskaraObject.__tojava__(Converte.class);
		
	}
	
}
