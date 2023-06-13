package imperative;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

import static imperative.Main.Gender.*;

public class Main {
    public static void main(String[] args) {
        List<Person> people = List.of(
                new Person("John", MALE),
                new Person("Maria", FEMALE),
                new Person("Alexa", FEMALE),
                new Person("Marin", MALE),
                new Person("Alex", MALE)
        );
        System.out.println("//Enfoque imperativo");
        //Enfoque imperativo
        List<Person> females = new ArrayList<>();

        for(Person person : people){
            if(FEMALE.equals(person.gender)){
                females.add(person);
            }
        }
        for(Person female : females){
            System.out.println(female);
        }
        System.out.println("//Enfoque Declarativo");
        //Enfoque Declarativo
        people.stream()
                .filter(person -> FEMALE.equals(person.gender))
                .collect(Collectors.toList())
                .forEach(System.out::println);


    }

    //clases persona con su contructor y un to string para presentar los datos
    static class Person{
        private final String name;
        private final Gender gender;


        Person(String name, Gender gender) {
            this.name = name;
            this.gender = gender;
        }

        @Override
        public String toString() {
            return "Person \n" +
                    "name= " + name  +
                    "\ngender= " + gender + "\n";
        }
    }

    enum Gender{
        MALE, FEMALE
    }

}
