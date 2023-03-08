package studia.puchy;

import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.datasource.DriverManagerDataSource;

import java.util.List;

public class Test {


    public static void main(String[] args) {
        DriverManagerDataSource datasource = new DriverManagerDataSource();
        datasource.setUrl("jdbc:oracle:thin:@//localhost:1521/ORCL3");
        datasource.setUsername("SYSTEM");
        datasource.setPassword("Oracle123");
        datasource.setDriverClassName("oracle.jdbc.OracleDriver");

        PuchyDAO dao = new PuchyDAO(new JdbcTemplate(datasource));

        List<Puszka> listPuszka = dao.listPuszki();
        System.out.println(listPuszka);

        Puszka puszka = dao.getPuszka(1);
        System.out.println(puszka);
        System.out.println(puszka.getSciezka());


    }
}
