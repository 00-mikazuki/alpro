package com.belajar;

public class Main {
  public static void main(String[] args) {

    // tipe data primitive (nilai max / min valuenya fix)
    // integer, byte, short, long, double, float, char, boolean

    // integer (satuan)
    System.out.println("===INTEGER===");
    int i = 10;
    System.out.println("nilai integer i = " + i);
    System.out.println("Nilai max = " + Integer.MAX_VALUE);
    System.out.println("Nilai min = " + Integer.MIN_VALUE);
    System.out.println("Besar integer = " + Integer.BYTES + " bytes");
    System.out.println("Besar integer = " + Integer.SIZE + " bit");

    // byte (satuan)
    System.out.println("\n===BYTE===");
    byte b = 10;
    System.out.println("nilai byte b = " + b);
    System.out.println("Nilai max = " + Byte.MAX_VALUE);
    System.out.println("Nilai min = " + Byte.MIN_VALUE);
    System.out.println("Besar byte = " + Byte.BYTES + " bytes");
    System.out.println("Besar byte = " + Byte.SIZE + " bit");

    // short (satuan)
    System.out.println("\n===SHORT===");
    short s = 10;
    System.out.println("nilai short s = " + s);
    System.out.println("Nilai max = " + Short.MAX_VALUE);
    System.out.println("Nilai min = " + Short.MIN_VALUE);
    System.out.println("Besar short = " + Short.BYTES + " bytes");
    System.out.println("Besar short = " + Short.SIZE + " bit");

    // long (satuan)
    System.out.println("\n===LONG===");
    long l = 10L; // L agar membedakan dgn int
    System.out.println("nilai long l = " + l);
    System.out.println("Nilai max = " + Long.MAX_VALUE);
    System.out.println("Nilai min = " + Long.MIN_VALUE);
    System.out.println("Besar long = " + Long.BYTES + " bytes");
    System.out.println("Besar long = " + Long.SIZE + " bit");

    // double (bilangan real / koma)
    System.out.println("\n===DOUBLE===");
    double d = 10.5d; // d membedakan double dgn float
    System.out.println("nilai double d = " + d);
    System.out.println("Nilai max = " + Double.MAX_VALUE);
    System.out.println("Nilai min = " + Double.MIN_VALUE);
    System.out.println("Besar double = " + Double.BYTES + " bytes");
    System.out.println("Besar double = " + Double.SIZE + " bit");
    
    // float (bilangan real / koma)
    System.out.println("\n===FLOAT===");
    float f = 8.5f; // f membedakan float dgn double
    System.out.println("nilai float f = " + f);
    System.out.println("Nilai max = " + Float.MAX_VALUE);
    System.out.println("Nilai min = " + Float.MIN_VALUE);
    System.out.println("Besar float = " + Float.BYTES + " bytes");
    System.out.println("Besar float = " + Float.SIZE + " bit");

    // char (karakter) berdasarkan ASCII 
    System.out.println("\n===CHAR===");
    char c = 'c'; // f membedakan char dgn double
    System.out.println("nilai char c = " + c);
    System.out.println("Nilai max = " + Character.MAX_VALUE);
    System.out.println("Nilai min = " + Character.MIN_VALUE);
    System.out.println("Besar char = " +Character.BYTES + " bytes");
    System.out.println("Besar char = " +Character.SIZE + " bit");

    // boolean (true / false)
    System.out.println("\n===BOOLEAN===");
    boolean val = true; // f membedakan boolean dgn double
    System.out.println("nilai boolean val = " + val);
    System.out.println("Nilai max = " + Boolean.TRUE);
    System.out.println("Nilai min = " + Boolean.FALSE);
  }
}
