package studia.puchy;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.namedparam.BeanPropertySqlParameterSource;
import org.springframework.jdbc.core.namedparam.NamedParameterJdbcTemplate;
import org.springframework.jdbc.core.simple.SimpleJdbcInsert;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public class PuchyDAO {

    @Autowired
    private JdbcTemplate jdbcTemplate;

    public PuchyDAO(JdbcTemplate jdbcTemplate) {
        super();
        this.jdbcTemplate = jdbcTemplate;
    }

    public List<Puszka> listPuszki() {
        String sql = "SELECT * FROM Puszki";
        return jdbcTemplate.query(sql, BeanPropertyRowMapper.newInstance(Puszka.class));
    }


    public Puszka getPuszka(int id) {
        Object[] args = {id};
        String sql = "SELECT * FROM Puszki WHERE id_puszki = ?";

        return jdbcTemplate.queryForObject(sql, BeanPropertyRowMapper.newInstance(Puszka.class), args);
    }


}
