import static java.time.Clock.system;
import javax.swing.JOptionPane;


public class tema1 {

    public void verdaderoAproximado(){
            double n1=0;
            double n2=0;
            double operacion=0;
            double operacion2=0;
            int negativo=-1;
            double resultado=0;
    
                operacion=n1-n2;
                resultado= operacion*negativo;
                
                
                JOptionPane.showMessageDialog(null, "El Error absoluto es: "+resultado);
                operacion2=operacion/n1*negativo;
                JOptionPane.showMessageDialog(null, "El Error Relativo es: "+operacion2);
                //prueba de decimal si funciona 
                //Natividad haz un submenu en donde llame esta operacion donde el usuario indique cuanto decimales desea quitar, haz lo mismo con los dos errores ahora solo lo hize con el absoluto
                resultado=resultado*1000/1000;
                JOptionPane.showMessageDialog(null, "El resultado decimal es "+String.format("Valor: %.2f", resultado));
                System.exit(0);
                
    }
    public static void main(String[] args) {
        tema1 v= new tema1();
        int opc(JOptionPane.showInputDialog(null, "Elija un tema"+"\n"+"1-TEMA 1"+"\n"+"5-Salir"));
        do {
            switch(opc){
            case 1:
                int te1(JOptionPane.showInputDialog(null, "Elija un subtema"+"\n"+"1-Errores"));
                do {
                    switch(te1){
                        case 1:
                            v.verdaderoAproximado();
                    break;
                    
                    default:
                    JOptionPane.showMessageDialog(null, "Elija al menos una opcion");}
                    
                } while (te1!=5);
                break;
            default:
                JOptionPane.showMessageDialog(null, "Elija al menos una opcion");
            }
            
        } while (opc!=5);
        
       

        
    }
}
