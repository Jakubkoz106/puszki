package studia.puchy;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
//import org.springframework.security.core.Authentication;
//import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

import java.util.List;

@Controller
@Configuration
public class AppController implements WebMvcConfigurer {

    @Autowired
    private PuchyDAO dao;


    @RequestMapping("/index")
    public String viewTablePageAdresy(Model model) {
        List<Puszka> listPuszka = dao.listPuszki();
        model.addAttribute("listPuszka", listPuszka);
        return "puchy-view";
    }

    @RequestMapping("/")
    public String viewTablePageAdresy2(Model model) {
        List<Puszka> listPuszka = dao.listPuszki();
        model.addAttribute("listPuszka", listPuszka);
        return "puchy-view";
    }

    @RequestMapping("/puchy/{id_puszki}")
    public ModelAndView showPuszka(@PathVariable(name = "id_puszki") int id_puszki) {
        ModelAndView mav = new ModelAndView("puszka-view");
        Puszka puszka = dao.getPuszka(id_puszki);
        mav.addObject("puszka", puszka);

        return mav;
    }



}
