package studia.puchy;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.datasource.DriverManagerDataSource;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class PuchyDAOTest {

    private PuchyDAO dao;

    @BeforeEach
    void setUp() throws Exception{
        DriverManagerDataSource datasource = new DriverManagerDataSource();
        datasource.setUrl("jdbc:oracle:thin:@//localhost:1521/ORCL3");
        datasource.setUsername("SYSTEM");
        datasource.setPassword("Oracle123");
        datasource.setDriverClassName("oracle.jdbc.OracleDriver");

        /* Import JdbcTemplate */
        dao = new PuchyDAO(new JdbcTemplate(datasource));
    }

    @Test
    void list() {
        /* Import java.util */
        List<Puszka> listPuszka = dao.listPuszki();
        assertTrue(listPuszka.isEmpty());
    }

//    @Test
//    void save() {
//        Adres adres = new Adres(0, "Warszawa",
//                "00-202", "Hutowa", 22, 1);
//        dao.saveAdres(adres);
//
//    }

    @Test
    void get() {
        Puszka puszka = dao.getPuszka(1);

        assertNotNull(puszka);
    }

//    @Test
//    void update() {
//        Adres adres = new Adres();
//        adres.setId_adresu(54);
//        adres.setMiejscowosc("Poddębice");
//        adres.setUlica("Dupna");
//        adres.setKod_pocztowy("05-220");
//        adres.setNr_domu(22);
//        adres.setNr_mieszkania(12);
//
//        dao.updateAdresy(adres);
//    }

//    @Test
//    void delete() {
//        dao.deleteAdres(4);
//    }
}