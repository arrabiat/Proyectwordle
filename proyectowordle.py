import random

palabras= ("apoyo", "amigo", "armar", "antes", "ayuda", "ahora", "abrir", "audaz", "ajeno", "aroma", "andar", "azada", \
           "agrio", "actor", "algún", "axial", "autor", "ancho", "avaro", "ahíto", "ameno", "astro", "avión", "aquel", \
           "agudo", "aviso", "arduo", "abuso", "apego", "alzar", "ansia", "atrio", "amado", "alado", "aunar", "anexo", \
           "ayuno", "atroz", "ardid", "atrás", "acero", "aovar", "abajo", "arena", "aéreo", "atajo", "azote", "atado", \
           "atril", "ajado", "ataúd", "asear", "ardor", "arder", "araña", "apodo", "asilo", "acoso", "abono", "aliar", \
           "añejo", "acaso", "aleta", "aojar", "axila", "alero", "apero", "asado", "aforo", "aldea", "apuro", "argot", \
           "ambos", "antro", "ajuar", "apear", "aguja", "acera", "asomo", "andén", "ahogo", "arcón", "arado", "arete", \
           "afear", "airar", "arada", "anuro", "amago", "andas", "amiga", "arreo", "arpón", "atañe", "abecé", "ardua", \
           "augur", "albur", "albor", "aliño", "alcor", "añoso", "autos", "arpía", "acedo", "aupar", "aleve", "adiós", \
           "arcén", "atlas", "alear", "acato", "arnés", "añico", "ajada", "apaño", "aloja", "alias", "abano", "ananá", \
           "ambón", "ancón", "añojo", "anglo", "arrea", "aljez", "alfar", "andel", "asere", "ascua", "adobo", "avatí", \
           "alajú", "arria", "adoso", "arpás", "alzan", "apoca", "alojo", "asgas", "avala", "aleja", "apana", "adoré", \
           "apoco", "aunad", "aliñé", "atusa", "alzás", "avalo", "alejo", "acusa", "atuso", "alisa", "acuso", "arded", \
           "aliso", "afean", "alela", "ahíla", "anota", "adosé", "alelo", "ahílo", "anoto", "afeás", "avalé", "alejé", \
           "apané", "atusé", "acusé", "alfan", "alisé", "afama", "alega", "alelé", "arpen", "añoja", "ahilé", "anoté", \
           "afamo", "alfás", "añosa", "alego", "alaba", "aboca", "añora", "arpes", "alabo", "ajear", "alcen", "aboco", \
           "añoro", "acata", "arpar", "alces", "aduce", "adula", "afila", "adulo", "afamé", "afilo", "aulós", "afeen", \
           "añado", "apiña", "auges", "abren", "añoré", "abole", "arpad", "afees", "abrís", "apiño", "animé", "abolo", \
           "aulas", "alojé", "adujo", "auras", "aísla", "apaga", "acaté", "alzad", "aduje", "adulé", "apega", "afilé", \
           "ajáis", "acude", "aíslo", "aviva", "alfen", "apago", "acuna", "abría", "araño", "acudo", "avivo", "acuno", \
           "añadí", "alfes", "apiñé", "apila", "abolí", "ajaba", "afead", "abrió", "apilo", "aíran", "azara", "alude", \
           "apean", "aislé", "azaro", "aludo", "arañé", "acudí", "aráis", "asume", "avivé", "acuné", "airás", "apeás", \
           "asumo", "añada", "alfad", "ajará", "apilé", "ajaré", "araba", "abran", "andan", "abola", "atiza", "argüí", \
           "aérea", "amoló", "azaré", "aludí", "atizo", "abras", "asada", "amolé", "agita", "asumí", "ahúma", "ajéis", \
           "acuda", "aboga", "agito", "ahúmo", "aducí", "abogo", "avisa", "arará", "alían", "araré", "aveza", \
           "aticé", "avezo", "agoró", "atáis", "aíren", "agoré", "aluda", "abrid", "apeen", "agité", "ahumé", "aréis", \
           "asuma", "aíres", "avena", "apees", "avisé", "atada", "ataba", "aveno", "agria", "avecé", "aguda", "atrae", \
           "anula", "andes", "anulo", "ahíta", "ahoga", "acnés", "airad", "atará", "avené", "apead", "amolá", "asean", \
           "ataré", "ajena", "amáis", "alada", "alíen", "aseás", "atina", "alíes", "anulé", "atino", "atéis", "arman", \
           "afluí", "ayudo", "amaba", "andad", "apena", "adoba", "aúlla", "apeno", "avara", "armás", "aúllo", "atiné", \
           "ayudé", "amará", "aliad", "ateza", "amasa", "amaré", "atezo", "apené", "amaso", "adobé", "aullé", "abusa", \
           "aseen", "améis", "azuza", "acaba", "aceza", "aúnan", "asees", "asana", "azuzo", "acabo", "acezo", "ansío", \
           "anega", "atecé", "amasé", "actúa", "anego", "armen", "aunás", "acoge", "arden", "actúo", "abusé", "acojo", \
           "amada", "asila", "armes", "ardés", "anuda", "asido", "azucé", "acabé", "anudo", "azota", "acecé", "ansié", \
           "ataja", "asead", "ardía", "azoto", "aboya", "actué", "aboyo", "ambas", "asían", "acogí", "amena", "albea", \
           "ardió", "albeo", "asilé", "altos", "armad", "asías", "anexé", "anudé", "apoda", "anché", "ahíja", "atajé", \
           "aloca", "aboyé", "aúnen", "ahíjo", "aloco", "albeé", "asirá", "adora", "aúnes", "aliña", "acoja", "ardan", \
           "asiré", "adoro", "ancha", "amaga", "apodé", "ardas", "arpan", "aneja", "agrié", "anexa", "adosa", "ahijé", "asgan",\
           "bajar","bella","bueno","breve","banal","basar","burdo","broma","brisa","bello","beber","bingo","burla","burro",\
           "barco","busca","bahía","baile","bravo","buena","banco","bruto","beodo","bogar","borde","bruja","barro","balón",\
           "besar","basto","banda","botón","bolso","botar","batir","bolsa","bulto","barra","bulla","berma","barca","brazo",\
           "bañar","barba","buque","brote","bando","bruma","bomba","bicho","brezo","buril","beato","brasa","bazar","blusa",\
           "bardo","bedel","brujo","busto","bufar","banca","boato","bordo","bufón","burgo","balsa","boina","broca","bajío",\
           "buche","breña","borla","bizco","bajón","betún","bamba","batel","boxeo","belén","bledo","bajel","bases","brega",\
           "bosta","bucle","bisel","botín","bache","bebés","bacín","bilis","bozal","bollo","bonos","biota","broza","balas",\
           "bucal","brete","badén","boyar","brota","bujía","borra","bolas","breva","bonus","beige","bombo","balda","binar",\
           "boira","bocón","batea","batín","bisar","bocal","bajos","boche","bureo","bongo","balde","bofia","bubón","berza",\
           "babel","belfo","bocel","batón","borna","buzar","braña","bemba","bizca","brego","borda","bañen","bañes","borré",\
           "bayos","baños","bañad","brava","bajan","bajás","beben","bruta","borró","burda","bebía","burra","bebió","baldo",\
           "barre","bogan","bajen","bisan","bogás","bríos","bajes","bisás","beban","boyan","barrí","bebas","birla","boyás",\
           "brama","birlo","bogué","bramo","bajad","basan","bulos","bebed","basás","birlé","besan","bramé","bisen","besás",\
           "buses","broto","bytes","bises","bulle","bacán","boyen","bullo","balín","boyes","búhos","bogad","bisad","bullí",\
           "babas","basen","boyad","besen","beses","bufan","bufás","burlo","basad","besad","burlé","bajía","bufen","bufes",\
           "baila","bares","bailo","beata","bañan","bufad","belfa","bucea","bañás","buceo","beoda","bozón","bezón","bembo","busco","buceé",\
           "crear","comer","causa","carta","claro","coger","calma","cerca","campo","culpa","común","capaz","cielo","copia","chico",\
           "ciego","clase","creer","color","curar","corte","culto","corto","clave","cauto","celos","casta","cinta","ciclo","calor",\
           "cerdo","cifra","carro","cargo","clima","clara","costa","calle","ceder","curso","cruel","chica","curva","citar","ceñir",\
           "chapa","cueva","cesar","canon","coche","cerro","carga","cagar","cabal","canal","caída","cutre","costo","cajón","chino",\
           "catar","carne","caber","circo","cisma","catre","callo","cavar","casar","coste","coser","coito","cuota","curvo","cirio",\
           "choza","cruce","cegar","cazar","crudo","cauce","censo","civil","cenit","coral","casto","canto","colar","calvo","cariz",\
           "cesta","clavo","cuero","chulo","canoa","celda","casco","calar","cable","cubil","colmo","cuate","cursi","cebar","cerco",\
           "caído","cabra","credo","cobro","cutis","crema","caqui","criba","cesto","cocer","caldo","cuita","chivo","cofre","calco",\
           "cacao","criar","cenar","cague","cejar","cirro","carpo","chola","curda","chuzo","calzo","cerne","calva","chalé","cisco",\
           "capón","clava","cidro","cieno","corsé","craso","carpa","canje","calmo","cinto","cojín","chile","cruza","corro","cacho",\
           "copla","cómic","china","comba","cafre","chato","cupón","cuasi","calza","compa","coima","cerda","chavo","cáliz","careo",\
           "caray","curia","críos","corvo","chava","copar","chepa","curro","cromo","curdo","chupa","corta","cagón","cisne","chamo",\
           "choto","cilla","cucar","carey","cuete","chiva","chala","casca","cacri","chozo","chito","coala","cuche","codal","clown",\
           "chiri","cumba","cávea","coiné","cebón","coyán","cónfr","chira","corra","cojas","cubro","cenen","creás","causé","chafa",\
           "cieis","cebos","copen","cundí","cenes","cobré","copes","cagad","caten","cubrí","címba","coged","creía","ceben","carea",\
           "copio","cosen","cebes","cenad","creyó","crina","cunda","cosés","crino","copad","coita","cenas","canes","canas","creen",\
           "cosía","cubra","capta","copié","careé","capto","catad","crees","cosió","cebad","criné","culea","coité","cazan","cuida",\
           "culeo","cuido","capté","cazás","clama","cread","cuaja","caben","clamo","citan","cimas","cosan","chora","culeé","choro",\
           "citás","cosas","cuidé","ciemo","creed","cabía","cipos","clamé","cuajé","choré","cosed","cesan","cacen","cabré","chuta",\
           "curvé","cesás","caces","chuto","colgó","caéis","cisca","citen","capos","canta","cojea","crían","ciñen","contó","caigo",\
           "caían","ceñís","cojeo","cites","conté","crias","chuté","caías","calcé","caras","calmé","ceñía","cerré","cribo",\
           "campa","canté","cojeé","curan","caerá","cabed","citad","cesen","caeré","calca","curás","clics","ceses","cubas","carda",\
           "cribé","cardo","cubos","campé","caiga","cuece","críen","colgá","ciñan","cocés","cabes","cuezo","cucos","cursa","comen",\
           "críes","ciñas","cocía","contá","cesad","cansa","cocas","comés","cardé","cauta","culpo","canso","coció","calla","comía",\
           "cocos","cerrá","curte","chivé","combo","cuajo","carpe","curra","curen","curto","cursé","comió","criad","ceñid","cures",\
           "culpé","cucan","cansé","ceden","crasa","cucás","combé","cifro","cerní","cedés","cacos","chalo","curtí","cadas","cueza",\
           "carpí","curré","codea","cupos","cedía","codeo","coman","casos","censa","curad","cruda","crece","cedió","cafés","comas",\
           "cuqué","cifré","cajas","curta","cuata","codeé","coced","chata","cagan","cacha","cogen","censé","cuños","cagás","chafo",\
           "cates","crecí","corre","colma","culta","cedan","comed","cogés","cenan","ciado","ciais","cedas","copan","cogía","choca",\
           "checa","choco","checo","chula","copás","chafé","cogió","ciaba","catan","ciega","corrí","colmé","ceban","cabro","catás",\
           "cucad","chota","ceded","cebás","causo","cunde","chama","cruzo","cobra","cundo","ciará","calós","camas","cavos","ciaré",\
           "cojan","cayos","crean","cubre","deseo","donde","decir","dulce","dejar","deber","dicha","dueño","dotar","débil","dolor",\
           "denso","dieta","donar","durar",\
           "dicho","danza","dudar","deuda","dosis","drama","dañar","docto","dócil","duelo","digno","droga","dogma","doble","diosa",\
           "disco","dardo","ducha","desde","domar","doler","dueto","dorso","demás","ducho","dique","dandi","dador","debut","dorar",\
           "duela","dátil","darse","ducto","diana","dueña","dable","diván","deudo","duplo","dombo","dundo","disón","dalle","depre",\
           "dunda","darás","dupla","dejan","dicen","daría","decís","dejás","duden","deben","dados","demos","dudes","dagas","densa",\
           "decía","daños","diere","debía","debes","dirán","debió","dudad","disca","dirás","danzo","diría","dejen","duché","digan",\
           "dejes","dedos","digas","dancé","deban","doñea","doñeo","debas","dista","disto","dejad","decid","doñeé","debed","dentó",\
           "denté","dobla","doblo","donan","dañan","dañás","desoí","dicta","dicto","desea","doran","dentá","dorás","dormí","divos",\
           "dotan","donen","dicté","dañen","dotás","deseé","dañes","duran","domas","donad","doren","dañad","dores","doman","dones",\
           "doten","dotes","doñas","dorad","digna","duren","dures","dotad","domen","diluí","dunas","durad","domes","duras","drena",\
           "dudan","dando","dreno","duros","damos","dudás","decae","draga","daban","domad","docta","drago","dabas","drené","dimos",\
           "diste","darán","decaí","etapa","estar","error","echar","enojo","ebrio","etnia","errar","envío","enano","extra","ejote",\
           "espía","efebo","esmog",\
           "entre","esnob","envés","equis","email","estro","erebo","enema","eolio","elepé","emito","ebria","educa","educo","echan",\
           "envié","emití","echás","emita","errad","elude","eludo","echen","enana","elige","eches","elijo","evade","eludí","evado",\
           "elegí","echad","eleva","elevo","evadí","eluda","expía","exime","expío","eximo","elevé","elija","evada","expié","eximí",\
           "eriza","erizo","evita","exima","ericé","evito","evité","entra","entro","están","edita","edito","estás","estoy","emana",\
           "emano","edité","exige","exijo","evoca","emané","erguí","evoco","estén","estés","exigí","eroga","erogo","estad","errás",\
           "exija","erais","envía","emite",\
           "feliz","final","forma","falta","frase","fácil","friki","flujo","flaco","firme","fútil","furor","fondo","fluir","fruto",\
           "falso","fijar","fauna","favor","fuera","firma","fuego","flojo","furia","faena","fallo","feroz","falaz","fósil","falla",\
           "fatal","fugaz","feria","fatuo","flora","fibra","fecha","finca","fruta","funda","falda","farsa","falto","farol","frito",\
           "fuero","fiera","fardo","flota","felón","fisco","freno","flete","ficha","flema","fusil","friso","feraz","fango","finta",\
           "freír","fobia","fiero","forro","fugar","farra","felpa","filón","fajar","fleco","focha","fumar","folio","fogón","flama",\
           "facha","fanal","filme","fuste","feudo","fasto","fusta","fonda","fosco","filia","finar","falúa","finge","flato","forja",\
           "fórum","figón","fosca","fosal","frote","fátum","fusis","farsi","fiemo","feuco","fleta","filos","formé","fuere","fines",\
           "fregá","forjo","finos","fugad","forjé","funja","filma","filmo","faeno","falsa","fisga","frota","froto","faené","fasta",\
           "floto","fiado","facas","fiais","foros","flaca","fríen","floja","floté","freís","fajan","fiaba","fajás","fiaca","freía",\
           "finto","fiará","falos","fiaré","ficho","forra","fisgo","famas","finté","frita","fieis","fríoa","floro","freta","freto",\
           "frían","fiché","finjo","fundí","fajen","forré","frías","fajes","floré","freté","finan","fingí","faros","filio","finás",\
           "freíd","fajad","fuman","fases","fumás","fundo","filié","finja","fluis","fulge","fluye","fuljo","fluyo","faces","fluía",\
           "fungi","fundé","finen","frena","fulgí","fumen","fumes","fugan","frené","fregó","fulja","fluya","fetos","finad","fugás",\
           "falté","fumad","fugué","formo","fluid","fijos","funge","funjo","freza","fresa",\
           "girar","globo","grito","gordo","ganar","grave","grato","gente","gozar","gusto","guapa","grado","guiar","guapo","gesto",\
           "ganas","genio","gasto","ganso","gruta","garbo","gesta","golfo","grano","gueto","gemir","gnomo","gorra","grasa","galán",\
           "guisa","ganga","guion","gorro","gramo","glosa","garra","gallo","grava","graso","guita","gafas","garzo","grumo","galón",\
           "gañir","galio","grajo","grelo","guiso","gafar","greña","guiri","gorda","garla","gozne","grifo","grima","gases","garúa",\
           "guasa","grana","gacha","gabán","grada","grama","galas","golfa","gubia","grupa","greda","guata","guano","grapa","gocho",\
           "guija","gofre","gongo","grifa","güito","gorja","güila","guzgo","gravo","gozás","grogs","grita","grúas","garlo","gocen",\
           "grité","goces","garlé","gruñe","ganan","gruño","gozad","grapo","guía*","gruñí","guían","gulas","guias","gimen","gemís",\
           "güifa","grapé","gemía","gruña","ganen","gimió","ganes","gusta","gasas","guíen","golea","goleo","guíes","giman","ganad",\
           "gusté","geles","gimas","gemas","graba","goleé","grabo","guiad","gañís","gemid","gasta","grabé","giran","gañía","galla",\
           "girás","gasté","giros","gises","gansa","garza","gallé","gloso","giren","goles","gires","glosé","gongs","gañid","gotas",\
           "graja","gozos","girad","guais","guisé","grata","guzga","graos","gozan","gesté","hacer","hecho","hueco","hábil","haber",\
           "honor","hogar","hasta","huevo","habla","hacia","huida","hobby","herir","hielo","horda","humor","héroe","harto","hilar",\
           "hueso","hurto","heces","hosco","hedor","harén","himno","helar","hebra","hondo","halar","halla","honra","hiato","hipar",\
           "hucha","hertz","horca","heder","hueva","hindú","hurón","hongo","hacha","huero","honda","horma","hotel","horro","hades",\
           "humus","heñir","hacho","hinco","huesa","hunda","hecha","hiera","halen","hendí","hales","huela","herid","herví","halad",\
           "hiela","helás","holgá","hacen","hendé","horra","hosca","hurga","hueca","hurgo","harán","hiele","harás","harba","haría",\
           "hemos","harbo","hagan","hagas","había","helad","hados","halas","harbé","halos","habrá","haced","habré","humea","humeo",\
           "hatos","hayas","haces","hazas","hayan","hilan","humeé","hilás","henos","habed","holló","hollé","hiede","hilen","hedés",\
           "hiedo","harté","hiles","hedía","humos","husos","hiñen","heñís","honro","hedió","heñía","hablo","hinca","hilad","honré",\
           "hollá","hojea","hallo","hurta","hojeo","hablé","hieda","hunde","herís","hiere","hundo","hiero","hiñan","hallé","halan",\
           "hojeé","hería","hurté","hiñas","heded","hifen","hirió","hundí","huele","huelo","heñid","hampa","harta","holgó","ideal",\
           "icono","igual","iluso","ijada","ileso","idear","ideas","impar","indio","impío","istmo","ixtle","inane","izado","idota",\
           "iraní","ilota","ibero","iones","insta","idead","islas","intuí","itera","irruí","itero","iteré","incoa","imbuí","incoo",\
           "ilesa","ilusa","incoé","izáis","imita","imito","izaba","imité","izará","izaré","icéis","idean","imán.","ibais","iréis",\
           "irían","irías","ideen","idees","jugar","jamás","joven","justo","juego","junto","jaula","jalar","jerga","jirón","junta",\
           "jaleo","judío","junco","justa","jabón","jadeo","joder","jarro","jarra","judas","jayán","jaque","juzga","jurar","jalón",\
           "judía","jamar","jamón","joyel","jiñar","jején","joyón","jamad","juega","jugás","jiñan","jacas","jacos","jugué","jiñás",\
           "jatos","jipío","jefes","jiras","jiñen","jiñes","jugad","jubos","jiñad","junté","jalan","juran","jalás","jipía","jurás",\
           "jipié","jalen","juren","jales","jures","jaman","jalad","jurad","jamen","james","juzgo","karma","koala","kéfir","kepis",\
           "khaki","koiné","kanes","kilos","largo","luego","lugar","lleno","libro","lento","libre","lindo","local","labor","lejos",\
           "listo","lecho","legal","logro","lucha","líder","linda","línea","llama","lista","letal","lucir","lápiz","legar","ligar",\
           "lobby","leche","lucro","lapso","lavar","letra","lycra","llave","llano","lanza","latir","laico","lerdo","labio","llaga",\
           "limar","limbo","labia","lloro","lamer","lente","latón","lábil","lijar","licor","libar","ligue","ligón","linfa","liceo",\
           "lacar","losar","luces","llena","lacra","lance","lacio","larva","lonja","linde","lauro","lunar","leído","litis","liado",\
           "lidia","lioso","leída","lampa","laxar","lasca","lince","ludir","ladeo","lanar","licra","laude","landó","llapa","lardo",\
           "luxar","lumia","losás","logré","lisia","lisio","ludid","leían","liará","liaré","leías","licuó","licué","lijad","lisié",\
           "lieis","leves","leerá","leyes","lleva","leños","leeré","llevo","liben","losen","libes","leáis","llago","loses","llevé",\
           "lavan","ligan","lides","laxan","lavás","libad","licuá","ligás","losad","laxás","lilas","labra","luxan","labro","libra",\
           "luxás","llora","liaza","labré","liras","laven","lidio","lisos","laxen","llamo","laxes","lites","lloré","lacan","lidié",\
           "llené","luxen","llamé","lenón","lacás","lavad","ligad","luxes","laxad","loado","loáis","laqué","liman","lapsa","larga",\
           "loaba","luxad","limás","lucen","lucís","loará","luzco","loaré","lucía","lenta","lerda","llega","lados","loéis","llego",\
           "lució","látex","lacad","limen","lajas","lamas","lamen","limes","lanas","laten","lamés","ladra","latís","ladro","liosa",\
           "lamía","lapos","lares","luzca","latía","luden","lamió","ludís","lanzo","limad","latió","lasos","ladré","ludía","lijan",\
           "latos","lucho","lucid","lijás","ludió","laman","listé","latan","laves","laxos","latas","luché","ludan","liais","logra",\
           "lamed","ludas","latid","liaba","lijen","liban","losan","lelos","lijes","libás","leéis","miedo","mucho","mujer","mundo",\
           "mejor","mayor","mirar","matar","manía","mismo","morir","medio","motor","meter","medir","mover","madre","monte","mente",\
           "motín","móvil","marco","marca","magia","moral","mando","mojar","mitad","metal","menos","media","menor","molde","mutuo",\
           "matiz","mitin","multa","manso","mueca","mimar","monje","malla","mixto","manar","mamar","morro","manta","musgo","minar",\
           "macho","moler","monto","mareo","mecha","monja","mudar","marea","magro","momia","morbo","merma","mitra","monta","magno",\
           "miope","morar","monda","matón","match","manto","mamón","mirlo","mirra","murar","meada","manda","mohín","mutar","modos",\
           "manir","mango","macis","muela","mosca","mural","mugre","mojón","molar","mudez","manga","mesón","mugir","mutis","musas",\
           "majar","maría","medra","mirón","metro","mande","meneo","mouse","mafia","mecer","magma","minga","medro","mocho","muñir",\
           "muslo","mitón","micho","memez","macha","maula","millo","mermo","mamas","morón","momio","malva","mosco","metra","miaja",\
           "manea","mújol","mazar","melgo","marlo","machi","mamúa","macia","marcí","majás","mohos","manad","miden","minen","marra",\
           "mojos","mareé","medís","marro","moles","mines","morid","marza","monas","marré","midió","mazos","mañas","minad","majen",\
           "monos","mutan","majes","mutás","midan","menea","mudan","medré","meten","midas","mudás","mecen","metés","mentó","mueso",\
           "majad","mecés","metía","meneé","mecía","medid","metió","malea","matan","melga","meció","maleo","matás","muten","memos",\
           "mentí","moros","mutes","muden","muñen","muñís","maleé","metan","mugen","mudes","mugís","mezan","muele","metas","monse",\
           "muñía","muelo","mezas","mutad","mugía","mentá","molía","motes","maten","mugió","mudad","molió","motos","meted","menús",\
           "meced","mella","mozas","maman","mozos","moran","miran","mello","muñan","misma","mujan","morás","mirás","misil","mixta",\
           "muñas","meros","matad","meses","mudos","masca","mujas","mesas","masco","mellé","manís","mallo","mueve","muñid","movés",\
           "muevo","mugid","moled","movía","manió","mamen","mallé","mojan","mondo","moren","miren","movió","mames","micos","mojás",\
           "mores","mires","mijos","mondé","miles","mamad","merca","morad","mirad","mueva","mordí","mimos","mista","merco","mucha",\
           "mapas","manan","manid","mares","morís","mojen","muere","muero","mutua","misté","mojes","moved","moría","minan","murió",\
           "minás","mojad","mizos","manen","marce","mordé","marzo","mases","manes","magna","magra","muera","majan","misto","mates",\
           "nuevo","nivel","norma","nunca","nacer","noche","niños","negro","notar","noble","nueva","nicho","negar","necio","norte",\
           "nieve","novio","ninfa","navío","niñez","nuera","nimio","nadar","novel","nariz","nylon","nimbo","naipe","nevar","natal",\
           "numen","níveo","naval","neura","nesga","nipón","napia","nidal","nadie","nauta","nenés","nublo","nones","norio","negus",\
           "nilón","nanay","nanái","noten","nublé","novia","notes","nubla","netos","notad","nexos","nidos","nodos","norme","notas",\
           "nubes","nucas","niega","negás","niego","normo","negué","nacen","nacés","nazco","nacía","nació","negad","nadga","nazca",\
           "narra","narro","nadas","naced","nanas","notan","narré","necia","negra","naves","nívea","ñandu","ñinga","ñisca","ñorda",\
           "ñoños","orden","otoño","ojalá","oveja","osado","optar","ocaso","obvio","oasis","obrar","obeso","omiso","ojota","ojear",\
           "ozono","opaco","ojera","otear","obice","odiar","oeste","otero","oxear","orate","okupa","ocupa","oreja","oidor","orgía",\
           "ornar","orina","orlar","orujo","ovino","opimo","obras","oliva","obesa","ojete","orear","oblea","oírse","osera","opina",\
           "oíble","osear","oídio","olote","ozona","ooide","oxeás","opten","olerá","optes","oleré","opone","orlan","oláis","orlás",\
           "optad","opuso","opuse","oxeen","obstó","obvia","obsta","oxees","obste","omisa","obvié","orlen","oxead","opaca","opima",\
           "orles","ornan","omina","opero","omino","ornás","osada","orlad","operé","ominé","ovina","opino","osean","oseás","opiné",\
           "ornen","ornes","ocupo","orado","oráis","ocupé","ornad","obran","oraba","ovado","oseen","ováis","osees","ovaba","orará",\
           "oraré","odian","osead","odiás","ocios","oréis","ovará","ocres","ovaré","obren","ovéis","odios","obres","odres","oímos",\
           "orino","oíais","ogros","odien","obrad","odies","oíste","ollas","oirán","oriné","oirás","otaku","onces","oiría","ondas",\
           "odiad","optan","oigan","optás","ocote","ocluí","oigas","oyere","olido","oléis","olían","olías","poder","perro",\
           "pedir","poner","parte","papel","punto","pasar","pluma","pobre","parar","pagar","parco","plano","pieza","pausa","pegar",\
           "punta","pasto","padre","playa","pesar","pelea","pisar","pista","pulso","prado","pacto","pilar","pompa","paseo","parca",\
           "pleno","pared","pavor","poeta","pauta","pulir","parra","presa","prisa","plazo","poema","picar","plato","plaza","porte",\
           "pugna","probo","peste","polvo","pasta","plaga","pudor","parir","patio","pasmo","prosa","pillo","panel","perla","pinta",\
           "pecho","preso","plata","prole","persa","pañal","peaje","perra","placa","porno","porra","primo","penar","pollo","pardo",\
           "podar","plebe","pizca","pecar","pesca","palma","prior","panza","piano","potro","pacer","pelar","piara","pasma","punir",\
           "pitar","peine","puzle","patán","plomo","piñón","pezón","picha","parné","purga","patín","papeo","profe","podio","pachá",\
           "prima","potar","peana","posar","parto","pulla","penal","poste","pifia","polla","puñal","parvo","ponto","pampa","púber",\
           "perol","penas","púgil","palmo","pujar","polar","pulpa","palco","parón","piola","pilón","panda","pelón","penco","potra",\
           "pingo","prora","parce","puyar","peñón","pitón","pocho","páter","paltó","pompi","pavés","palca","paila","punía","plisé",\
           "pobló","pulas","puyes","poblé","plena","paren","pedía","punió","preví","pocha","pares","piaré","penes","pidió","pulsé",\
           "pegan","pulid","puros","puyad","priva","pican","privo","pegás","pieis","parid","puyas","punan","puños","pasen","parad",\
           "peras","punas","pidan","pases","privé","pocos","pegué","pidas","pilan","piqué","poblá","prava","ponen","placo","pilás",\
           "punid","plegó","pasad","pasea","ponés","pongo","pedid","ponía","penan","pravo","paseé","pagan","pegad","pagás","pilen",\
           "porta","proas","picad","porto","peros","piles","posee","ponga","poseo","plegá","peleo","pagué","primé","penen","pisan",\
           "pesan","pilad","profa","palió","poseí","pisás","palié","poned","pesás","peleé","parda","plañe","palmé","penad","pifio",\
           "pesos","palpa","pecan","posea","palpo","pasmé","pacta","plañí","pecás","pelan","papea","petos","pagad","pifié","pelás",\
           "peces","pisen","pesco","partí","pesen","palpé","pacen","pudre","pudro","peses","pequé","picas","pacté","pacés","pazco",\
           "paliá","papeé","pacía","picos","pinto","parta","pació","pisad","probé","pesad","pelen","pugno","pijos","pinté","puede",\
           "peles","podés","puedo","pudra","pilla","podía","palea","pazca","paleo","pecad","perdí","pugné","pelad","podrá","pulen",\
           "puyan","pillé","pulís","podré","paleé","paced","parís","pises","probá","pipís","paran","pisos","pulía","posta","pueda",\
           "paría","place","parás","pitos","pulió","piñas","peina","parió","peino","piado","plisa","piais","pliso","punen","perdé",\
           "prevé","punís","pasan","plací","poded","plana","piaba","pulan","piden","puyen","pelos","pasás","pedís","pulsa","queja",\
           "quedo","quizá","quema","quita","quien","queda","quepí","quiui","quemé","quedé","quepo","quito","quité","quiso","quepa",\
           "quise","queré","quemo","regla","rumbo","razón","rueda","regar","robar","recto","resta","rubro","rigor","regir","ruido",\
           "rogar","ritmo","rabia","rival","raudo","rural","resto","rasgo","raspa","rezar","relax","rayar","ruina","ratón","radio",\
           "rozar","regio","rumor","rango","reino","rocío","rampa","revés","rodar","rollo","ronda","reina","ruego","rubio","rugir",\
           "rodeo","reñir","raído","recio","rapto","robot","rehén","rotar","rubor","rizar","renta","roído","rimar","riego","ronco",\
           "rosca","redil","rasar","rasca","retal","rucio","rumia","racha","rojez","ropón","ralea","remar","rapaz","recua","rajar",\
           "rever","rocín","rumba","retar","recta","rapar","riada","reata","rorro","ramal","ruedo","rifar","reses","rengo","rabal",\
           "rular","rilar","renga","renco","rezno","razia","riata","rolla","rento","roque","róseo","rolde","rozno","round","rusco",\
           "redor","razar","rucho","rasea","rallé","ruega","raseo","rogás","rapen","reglo","riman","rapes","rimás","raseé","rogué",\
           "rinde","roben","rindo","roten","reglé","robes","rigen","rotes","regís","rapad","rulan","rugen","regad","rulás","rugís",\
           "rendí","rondo","robad","rugía","rotad","rigió","rimen","rudos","rimes","rugió","rondé","roída","rulos","rinda","reiné",\
           "rogad","rijan","rozan","rósea","rulen","rubia","rimad","rijas","rubra","rozás","rucha","rujan","rodea","rucia","rules",\
           "rujas","risca","reman","risco","remás","regid","rarea","rodeé","rulad","rareo","rayan","rugid","rollé","rizan","rayás",\
           "rocen","repta","riela","relee","rizás","repto","rareé","rielo","releo","roces","riñen","raijo","reñís","remen","remes",\
           "repté","rielé","rapta","releí","rifan","reñía","rozad","rabio","rifás","reúne","rayen","reúno","rilan","ricen","rayes",\
           "remad","rapté","relea","rilás","rices","rabié","reuní","raspo","riñan","rezan","rayad","riñas","reído","rezás","rizad",\
           "rifen","rumio","raspé","reían","rifes","raída","ronza","reúna","reías","ronzo","reñid","rilen","reble","rumié","rauda",\
           "riles","reirá","ripio","rifad","roncé","renté","rabel","reiré","rocía","recen","radia","reces","rompe","rigil","riais",\
           "rilad","resté","rompo","riere","rocié","radié","rapan","rezad","rompí","rapás","regia","riega","regás","ralla","roban",\
           "rallo","rotan","robás","rotás","rasco","rehuí","rompa","renca","regué","salir","según","subir","saber","sacar","snack",\
           "sabio","soñar","suave","señal","salud","spray","señor","senda","serio","sobre","suelo","sucio","sueño","sello","stock",\
           "sumar","signo","sutil","serie","sagaz","shock","staff","stand","silla","sitio","salón","socio","sanar","sabor","senil",\
           "soler","surco","susto","sudar","salto","santo","símil","súper","secar","semen","selva","salvo","short","sesgo","sobra",\
           "sopor","sudor","saldo","savia","saeta","soplo","solaz","sorna","sonda","segar","secta","simio","sílex","solar","sarta",\
           "sorbo","scout","sable","siega","sarao","sarna","sobar","senos","sazón","speed","satén","sacho","sosia","salva","sucia",\
           "sismo","señas","sacro","seudo","sumir","segur","saque","sigla","sisar","silba","sirga","sarro","sufra","solio","sajar",\
           "satán","sayón","siglo","solfa","sapos","salsa","siete","suplo","sigan","sumió","sitié","sudás","sorbe","sisan","sequé",\
           "sentó","sobad","silbé","sigas","senté","serán","sanad","sisás","serás","suplí","sorbí","seáis","suena","sonás","suele",\
           "signa","solés","supla","suden","solía","salen","seres","sondo","sudes","salís","sorba","sisen","sumid","sufre","secad",\
           "salgo","sufro","sises","signé","sentá","suben","salía","subís","sondé","salió","sudad","subía","sufrí","sesos","surjo",\
           "suene","sisad","setos","suela","sacia","subió","sexos","sacio","saben","suman","shows","surgí","soldó","salga","sabés",\
           "soldé","sonad","sabia","sacié","soled","suban","sacra","subas","sopla","soltó","surja","solté","salvé","salid","sacón",\
           "sabrá","santa","sabré","sella","silos","sagas","simas","subid","sales","salas","sepan","soplé","sirve","sumen","sirvo",\
           "sepas","sumes","sanea","sellé","salda","saneo","soldá","sitúa","sitúo","sacan","serví","sacás","sabed","sumad","saneé",\
           "soltá","saldé","situé","surca","seria","sesga","sirva","sumas","sanos","sajan","sedar","sajás","simia","salan","salar",\
           "sibil","soban","socia","sañas","sebos","sanan","secas","sacad","sobás","secos","sentí","sajen","sajes","sigue","sobro",\
           "sedes","sajad","soben","secan","sumís","seguí","sitia","sanen","sobes","salad","surge","somos","silbo","sanes","sumía",\
           "suple","sudan","tener","tocar","tomar","tenaz","tarea","tanto","tarde","traer","total","temor","texto","tonto","turno",\
           "tejer","tapar","tenue","trama","trato","topar","tirar","tenia","tumba","torpe","tesis","trozo","temer","tapia","techo",\
           "terco","tosco","tedio","toque","tenso","tumor","truco","turba","teñir","timón","torre","tacto","telar","traje","trino",\
           "treta","traba","tañer","tribu","tutor","trazo","tenis","tabla","trago","torta","tieso","tasar","timar","temas","tropa",\
           "terso","tallo","trapo","trono","talud","tibia","talla","tapón","titán","talar","tinte","talle","tórax","tramo","tesón",\
           "tirón","torso","tifón","tonel","trola","tocón","tocho","tardo","trigo","tacón","trova","talón","tarja","tanda","tótem",\
           "tenca","túnel","tapiz","tempo","traza","tenor","tacha","tarro","tunda","toldo","testa","tajar","tetas","trote","tumbo",\
           "tacho","tropo","torvo","tarta","tripa","tambo","traga","terna","tizne","tasca","tiara","terno","tibio","tebeo","trabe",\
           "tilde","tisis","turca","telón","troje","tordo","taita","trusa","taxón","tique","trena","tabes","tunco","tilín","tiros",\
           "toril","tizón","toche","tupir","tarma","tentá","toreo","tupan","tajos","temen","tales","tupas","trocó","tasan","tejed",\
           "temés","timan","tasás","toreé","temía","timás","tanta","trina","tarda","temió","tañen","tupid","tebea","tañés","tesen",\
           "torcí","treme","troná","tremo","tañía","tríos","teses","toman","triné","traed","teman","tules","tomás","tulle","tensa",\
           "tullo","tasen","tajan","turna","timen","tremí","tupés","tases","trocá","tajás","terca","times","tesad","tersa","tañan",\
           "tullí","turné","tutes","temed","talan","tañas","tiesa","trema","tasad","techa","trata","timad","talás","torcé",\
           "toros","tomen","tomes","tulla","tocha","tajen","tañed","teché","traté","tonta","tajes","torda","tendí","torva","tomad",\
           "tosca","taché","talen","triza","tibié","tajad","trizo","turbo","timba","tricé","turbé","talad","trovo","tapan","tapás",\
           "tendé","tiran","trové","tunca","tumbé","tirás","tapen","tanga","tango","tapes","tinta","tiene","tiren","tenés","tinto",\
           "tengo","tires","tesar","tejen","tauca","tapad","tensé","tejés","tentó","teste","tejía","tenté","tirad","tupen","torna",\
           "tupís","tapio","tejió","torno","trota","tupía","troto","tenga","traen","tapié","tupió","torné","traés","tejan","trabo",\
           "traía","tejas","troné","tesan","tabús","tened","tracé","trajo","torea","tesás","unión","ufano","usted","urdir","usado",\
           "usual","unido","untar","ujier","urgir","usura","ultra","ungir","uncir","ucase","urubú","urdid","ulula","ululo","usáis",\
           "ubica","ululé","ubico","usaba","upado","usará","ubres","upáis","usaré","upaba","uséis","upará","untos","uparé","urbes",\
           "urnas","upéis","uncen","uncís","uncía","ufana","unció","usada","unzan","unzas","unían","urden","unías","urdís","urdía",\
           "uncid","unirá","uniré","urdió","unáis","urdan","urdas","valor","vacío","viaje","volar","venta","viejo","vivir","vasto",\
           "veloz","visto","valla","verde","voraz","vicio","vital","veraz","velar","valle","vigor","vuelo","vista","venir","valer",\
           "vejez","venia","verbo","vapor","virus","vagar","vedar","vetar","vivaz","verso","votar","vacuo","vejar","valía","vario",\
           "viril","vagón","vulva","vulgo","varón","video","visar","vello","venda","vasco","váter","vivac","vamos","verse","villa",\
           "virar","verja","vaina","vigía","venal","verga","visor","véase","verme","vacar","velón","voacé","vezar","valva","viñas",\
           "vence","valgo","venzo","venid","viven","vivar","vivís","volvé","vende","vendo","valió","volcá","vencí","vivía","visen",\
           "vises","vacan","vivió","vejen","vendí","votos","vacás","voces","vejes","valga","venza","visad","vivan","vaqué","vetan",\
           "vejad","vivas","vetás","valed","varea","vareo","vivid","versa","viran","vareé","virás","vinea","vacía","vineo","veten",\
           "viaja","vacad","viajo","vetes","vineé","vacié","vertí","viste","vetad","viren","vires","vestí","ventó","venté","vuela",\
           "volás","virad","vemos","vallo","veían","verté","veías","vimos","vados","verán","vives","vagos","verás","vahos","votan",\
           "vacua","vería","vales","vuele","votás","veáis","vezan","vivad","varia","vocea","vasca","vezás","voceo","vasta","viere",\
           "volad","venís","viene","vanos","vengo","varié","voceé","voten","viola","votes","volví","violo","vecen","volcó","vieja",\
           "veces","visan","violé","votad","venga","visás","vayan","vejan","vezad","vayas","valen","vejás","yerno","yacer","yerro",\
           "yermo","yelmo","yerba","yogur","yerto","yunta","yegua","yesca","yerna","yersi","yoqui","yocas","yerma","yerta","yacen",\
           "yacés","yacía","yació","yanta","yanto","yates","yayos","yemas","yanté","yucas","yutes","yaced","yendo","zorro","zurdo",\
           "zafio","zanja","zafar","zaino","zueco","zarza","zurra","zonzo","zagal","zambo","zafra","zanco","zuñir","zorra","zarpa",\
           "zurda","zumba","zaque","zarco","zoclo","zanca","zureo","zarpé","zaina","zamba","zarca","zurce","zurzo","zafan","zampa",\
           "zampo","zafás","zurcí","zampé","zurza","zafen","zumbo","zafes","zagas","zumbé","zanjo","zafad","zares","zedas","zetas",\
           "zanjé","zonas","zotes","zuros","zuñen","zuñís","zuñía","zuñan","zuñas","zuñid","zarpo")

def gris(letra):  
    
 
    for i in palabras:    
        if(i[0]!=letra and i[1]!=letra and i[2]!=letra and i[3]!=letra and i[4]!=letra):               
            wordles.append(i)
        
   
def amarillo(letra,posicion):
    wordles2=[]
    for i in palabras:      
        if(i[0]==letra or i[1]==letra or i[2]==letra or i[3]==letra or i[4]==letra):
            wordles2.append(i)
    
    for i in wordles2:
        if(posicion==0):
            if (i[0]!=letra) :
                wordles.append(i)
        if(posicion==1):
            if (i[1]!=letra) :
                wordles.append(i)
        elif(posicion==2):
            if (i[2]!=letra) :
                wordles.append(i) 
        elif(posicion==3):
            if (i[3]!=letra) :
                wordles.append(i)
        elif(posicion==4):
            if (i[4]!=letra) :
                wordles.append(i)
        
            
def verde(letra,posicion):
                
    for i in palabras:      
        if(posicion==0):
            if (i[0]==letra) :
                wordles.append(i)
        elif(posicion==1):
            if (i[1]==letra) :
                wordles.append(i)
        elif(posicion==2):
            if (i[2]==letra) :
                wordles.append(i) 
        elif(posicion==3):
            if (i[3]==letra) :
                wordles.append(i)
        else:
            if (i[4]==letra) :
                wordles.append(i)

wordles=[]

for i in range(6):
    wordle=random.choice(palabras)

    print(wordle)

    count=0
    
    for i in wordle:
        wordles=[]
        if(i=="á"):
            i="a"
        if(i=="é"):
            i="e"
        if(i=="í"):
            i="i"
        if(i=="ó"):
            i="o"
        if(i=="ú"):
            i="u"
        color = input(f"De que color es la letra {i}: ")
        if(color=="g"):
            gris(i)        
        if(color=="a"):
            amarillo(i,count)
        if(color=="v"):
            verde(i,count)
        count+=1
        palabras=tuple(wordles)
        print(palabras)
    