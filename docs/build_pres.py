from copy import deepcopy

from pysli.content import make_video_block, make_image_block, make_text_block 
from pysli.single_column import make_single_column
from pysli.double_column import make_double_column
from pysli.title import make_title 

#
#def make_single_column(\
#      title: str,\
#      header: str,\
#      top_page: str,\
#      slides: list[str],\
#      slide_idx: int,\
#     content_str: str,\
#     caption: str,\
#     subheader: str="",\
#     after_fold: str="",\
#     ) -> str:
#
#def make_double_column(\
#    title: str,\
#    header: str,\
#    top_page: str,\
#    slides: list[str],\
#    slide_idx: int,\
#    content_str_0: str,\
#    content_str_1: str,\
#    caption: str,\
#    subheader: str="",\
#    after_fold: str="",\
#    ) -> str:
#
#def make_video_block(video_path: str,\
#    video_link: str,\
#    video_alt_text: str,\
#    thumbnail_path: str=i'',\
#    use_autoplay: bool=False,\
#    caption: str="",\
#    height: int=512,\
#    width: int=512) -> str:
#
#def make_image_block(image_filepath: str,\
#    link: str,\
#    image_alt_text: str="",\
#    image_width: int=90,\
#    caption: str="",\
#    ) -> str:
#
#def make_text_block(bullet_points: list,\
#    paragraph: str="") -> str:
#
#def make_title(\
#    title: str,\
#    header: str,\
#    top_page: str,\
#    slides: list[str],\
#    slide_idx: int,\
#    content_str: str,\
#    subheader: str="",\
#    author: str="",\
#    date: str="",\
#    location: str="",\
#    caption: str="",\
#    ) -> str:

def update_slides_list(slide_makers, slide_maker, slides, slide_index):
  slide_name = f"{basename}_{slide_index:03}.html" 
  slides.append(slide_name)
  slide_index += 1

  slide_makers.append(deepcopy(slide_maker))

  return slide_makers, slides, slide_index

# setting up
basename = "pcbsaso"
slide_index = 0
htmls = []
slides = []
slides_kwargs = []
slide_makers = [] 
top_page = f"{basename}_{slide_index:03}.html" 

slide_function = make_title
slide_maker = {}
slide_kwargs = {}

# [ ] title slide 

slide_maker["function"] = slide_function
slide_kwargs["title"] = basename
slide_kwargs["header"] = "Planetary Cybernetics by Selection and Self-Organizaiton"
slide_kwargs["slide_idx"] = slide_index
slide_kwargs["author"] = "Rive Sunder" # update this TODO 
slide_kwargs["date"] = "2025/09/05"
slide_kwargs["location"] = "TOKYO VENTURE CAPITAL HUB 東京市港区"
slide_kwargs["caption"] = "<em><a href='https://www.tokyoai.jp/'>Tokyo AI</a></em>"
slide_kwargs["top_page"] = top_page



image_kwargs = {"image_filepath": "assets/coevo_summer_1983_dw_fig3.png",\
    "link": f"{basename}_{slide_index+1:03}.html",\
    "image_alt_text": "Planetary Cybernetics. click! If you want. I'm an alt text, not your master.",\
    "image_width": 60,\
    "caption": "From James Lovelock 'Daisy World: A Cybernetic Proof of the Gaia Hypothesis' "\
        "in <a href='https://archive.org/details/coevolutionquart00unse_34'>Coevolutionary Quarterly Summer 1983, p. 68</a>"}

image_str = make_image_block(**image_kwargs)

slide_kwargs["content_str"] = image_str

# will need to update this for all slides
slide_maker["slide_kwargs"] = slide_kwargs


slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)

# [ ] second title slide (with animation)

slide_kwargs["slide_idx"] = slide_index
slide_name = f"{basename}_{slide_index:03}.html" 
image_str_1 = make_image_block(image_filepath="assets/coevo_dw_glaberish6.gif",\
    link=f"{basename}_{slide_index+1:03}.html",\
    image_alt_text="Planetary Cybernetics. click! If you want. I'm an alt text, not your master.",\
    image_width=60,\
    caption="From James Lovelock 'Daisy World: A Cybernetic Proof of the Gaia Hypothesis' "\
        "in <a href='https://archive.org/details/coevolutionquart00unse_34'>Coevolutionary Quarterly Summer 1983, p. 68</a>")

slide_kwargs["content_str"] = image_str_1

slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)

slide_maker["function"] = make_single_column
points = []
points.append("Introduce the confluence of concepts")
points.append("a. Overview of daisyworld and descendants")
points.append("b. Self-organisation in cellular automata (CA)")
points.append("Evolution strategies and specification gaming")
points.append("The evolution will not be supervised")
points.append("Plausible self-organisation in DaisyWorlds")
points.append("CA with DaisyWorld characteristics")
points.append("Why? SETL, OOL, and dynamic planetary boundaries(?)")
points.append("End")

text_content = make_text_block(bullet_points=points)
slide_kwargs = deepcopy(slide_makers[-1]["slide_kwargs"])
slide_kwargs.pop("author")
slide_kwargs.pop("date")
slide_kwargs.pop("location")

slide_kwargs["content_str"] = text_content
slide_kwargs["header"] = "Talk outline"
sc_slide_kwargs = deepcopy(slide_kwargs)

slide_maker["slide_kwargs"] = slide_kwargs

slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)

slide_kwargs = deepcopy(slide_makers[-1]["slide_kwargs"])
slide_kwargs.pop("content_str")

# public domain source: 'https://commons.wikimedia.org/wiki/File:Gaia_(Kylix_detail).jpg'
image_1_path = "assets/gaia_kylix_detail.jpg"
# from Davis & Bongard 2022, "halting unpredictablity"
# https://dl.acm.org/doi/10.1145/3520304.3529037 https://arxiv.org/abs/2204.07541 https://raw.githubusercontent.com/riveSunder/yuca_docs/master/assets/halting_evo/pos237s1.pdf
image_2_path = "assets/gif_exp_s613_pattern_1645038142_end_107_elite0_0991.gif"

image_kwargs = deepcopy(image_kwargs)
image_kwargs["image_filepath"] = "assets/gif_exp_s613_pattern_1645038142_end_107_elite0_0991.gif"
image_kwargs["link"] = "assets/gif_exp_s613_pattern_1645038142_end_107_elite0_0991.gif"
image_kwargs["image_alt_text"] = "From Davis and Bongard 2022a: _Selecting ... for halting unpredictability_" 
image_kwargs["caption"] = "<strong>Self-organisation in CA</strong>. Evolved synthesis pattern from <a href='https://arxiv.org/abs/2204.07541' title='ArXiV:2204.07541'>Davis and Bongard</a> (<a href='https://dl.acm.org/doi/10.1145/3520304.3529037'>2022a</a>)"
image_kwargs["image_width"] = 80

image_content_left = make_image_block(**image_kwargs) 

image_kwargs = deepcopy(image_kwargs)
image_kwargs["image_filepath"] = "assets/gaia_kylix_detail.jpg"
image_kwargs["link"] = "assets/gaia_kylix_detail.jpg"
image_kwargs["image_alt_text"] = "Whoa, whoa. Detailed line drawing of Gaia from a 5th century BCE Greek kylix" 
image_kwargs["caption"] = "<br>A planetary cybernetics view holds that <strong>Life has an impact on planetary conditions</strong><br>-and-<br><strong>That impact collectively maintains habitable conditions"

image_content_right = make_image_block(**image_kwargs) 
#<!-- Image of Gaia drawn from a 5th century BCE red-figure <a href='https://en.wikipedia.org/wiki/Kylix' title='a wide, handled drinking cup from the ancient Greek pottery tradition.'>kylix</a> ( <a href='https://commons.wikimedia.org/wiki/File:Gaia_(Kylix_detail).jpg'>from Wikimedia Commons.</a>"-->

slide_kwargs["content_str_0"] = image_content_left
slide_kwargs["content_str_1"] = image_content_right
dc_slide_kwargs = deepcopy(slide_kwargs)

slide_kwargs["header"] = "Mixing self-organisation and selection-based control"
slide_maker["function"] = make_double_column
slide_maker["slide_kwargs"] = slide_kwargs
slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)

# [ ] 1983 daisyworld (a)
points = []
points.append("<strong>James Lovelock</strong>, influenced by life-detection research, develops the 'Gaia hypothesis'"\
    "(<a href='https://www.jameslovelock.org/planetary-atmospheres-compositional-and-other-changes-associated-with-the-presence-of-life/'>1965</a>, <a href='https://www.sciencedirect.com/science/article/abs/pii/0004698172900765?via%3Dihub'>19</a><a href='https://www.jameslovelock.org/gaia-as-seen-through-the-atmosphere/'>72</a>, <a href='https://ia802804.us.archive.org/12/items/LovelockMargulis1973/Lovelock-Margulis-1973.pdf'>1973</a>) ")
points.append("Skeptics include Richard Dawkins (<a href='https://en.wikipedia.org/wiki/The_Extended_Phenotype'>1982</a>) and W. Ford Doolittle (<a href='https://archive.org/details/coevolutionquart00unse_25/page/58/mode/2up'>1981</a>)")
points.append("<strong>Dawkins</strong>: 'The Universe would have to be full of dead planets whose homeostatic regulation systems had failed, with, dotted around, a handful of successful, well-regulated planets of which Earth is one.' and '[...] we would have to postulate some kind of reproduction, whereby successful planets spawned copies of their life forms on new planets.'")
points.append("<strong>Doolittle</strong>: 'I do not doubt that some of the feedback loops which Lovelock claims exist do exist, but I do doubt that they were created by natural selection, or that they are anything but accidental.' ")
points.append("<strong>Andrew Watson and James Lovelock</strong> describe a mathematical model, daisyworld, that uses selection to maintain habitable temperatures (<a href='https://archive.org/details/coevolutionquart00unse_34/page/66/mode/2up'>1983a</a>, <a href='https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1600-0889.1983.tb00031.x'>1983b</a>)")

points2 = []
points2.append("<strong>Dawkins</strong>: 'oxygen production as a byproduct of plant activity' ... 'we have been selected to breathe oxygen partly because there is so much of it about' ")
points2.append("Doolittle goes on to suggest that organisms manipulating their environment to maintain habitability would be like organisms (e.g. humans) somehow manipulating the physical constants of our Universe to give rise to life")


text_content = make_text_block(bullet_points=points)
after_fold_text = make_text_block(bullet_points=points2)

slide_kwargs = deepcopy(sc_slide_kwargs)
slide_kwargs["header"] = "Planetary cybernetics timeline"
slide_kwargs["content_str"] = text_content
slide_kwargs["after_fold"] = after_fold_text

slide_maker["function"] = make_single_column
slide_maker["slide_kwargs"] = slide_kwargs
slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)

# [ ] dw figure

image_kwargs = deepcopy(image_kwargs)
image_kwargs["image_filepath"] = "assets/daisyworld_1983_rs.png"
image_kwargs["link"] = "assets/daisyworld_1983_rs.png"
image_kwargs["image_alt_text"] = "A plot of the 0D daisyworld model showing light and dark daisies maintaining a habitable range of temperatures under progressively increasing stellar luminosity." 
image_kwargs["caption"] = "<tt>daisyworld</tt> is a 0-dimensional model described in (<a href='https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1600-0889.1983.tb00031.x'>AWJL 1983</a>). Light and dark-albedo daisies affect temperature, which in turn determines their growth rate, closing an <a href='https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2006RG000217'>antagonistic rein control</a> feedback loop."

image_content_dw = make_image_block(**image_kwargs) 

slide_kwargs = deepcopy(sc_slide_kwargs)

slide_kwargs["header"] = "<tt>daisyworld</tt> (Watson & Lovelock 1983)"
slide_kwargs["content_str"] = image_content_dw
slide_kwargs["after_fold"] = "" #after_fold_text # TODO image content for dw equations
slide_maker["function"] = make_single_column
slide_maker["slide_kwargs"] = slide_kwargs
slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)

# [ ] self-organisation from Life to Lenia and NCA
points = []
points.append("<strong>John von Neumann</strong> (+Stanislaw Ulam) and <strong>John Horton Conway</strong> develop CA and the Game of Life with replication, construction, and complexity in mind ().")
# add a bit about varela and maturana, 
points.append("Richard Guy discovers the reflex glider in Life (~1970)") #, Maturana and Varela, R.D. ")
#points.append("a lot of other things happen")
points.append("Stephan Rafler describes a glider in SmoothLife (<a href=''>2014</a>) ")
points.append("Bert Chan develops an expansive taxonomy of <span title='I like the term _pseudorganisms_ here'>solitons</span> in Lenia (<a href='https://www.complex-systems.com/abstracts/v28_i03_a01/'>2019</a>, <a href='https://chakazul.github.io/Lenia/JavaScript/Lenia.html'>web</a>)")
points.append("Growing neural cellular automata (<a href='https://distill.pub/2020/growing-ca/'>Mordvintsev <em>et al.</em> 2020</a>), Asymptotic Lenia (<a href='https://direct.mit.edu/isal/proceedings/isal2021/33/91/102916'>Kawaguchi <em>et al.</em> 2021</a>), Glaberish (<a href='https://direct.mit.edu/isal/proceedings/isal2022/34/47/112267'>Davis <em>et al.</em>2022</a>), and many more recent developments.")


text_content = make_text_block(bullet_points=points)
#after_fold_text = make_text_block(bullet_points=points2)

slide_kwargs = deepcopy(sc_slide_kwargs)
slide_kwargs["header"] = "A sampling of self-organisation in CA"
slide_kwargs["content_str"] = text_content
slide_maker["function"] = make_single_column
slide_maker["slide_kwargs"] = slide_kwargs
slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)

# [ ] self org CA gifs
image_kwargs = deepcopy(image_kwargs)
image_kwargs["image_filepath"] = "assets/s11_slow.gif"
image_kwargs["link"] = "assets/s11_slow.gif"
image_kwargs["image_alt_text"] = "An evolved slow glider in an evolved CA rule s11 from the glaberish CA family" 
image_kwargs["caption"] = "A slow glider emerging from an evolved synthesis pattern in an evolved CA rule s11 in the glaberish CA family"

image_content_left = make_image_block(**image_kwargs) 

image_kwargs = deepcopy(image_kwargs)
image_kwargs["image_filepath"] = "assets/frog_race.gif"
image_kwargs["link"] = "assets/frog_race.gif"
image_kwargs["image_alt_text"] = "An evolved hopping glider(s) in an evolved CA rule s11 from the glaberish CA family" 
image_kwargs["caption"] = "A group of 'hopping' gliders emerging from an evolved synthesis pattern in an evolved CA rule s643. From (<a href='https://direct.mit.edu/isal/proceedings/isal2022/34/47/112267'>Davis <em>et al.<em> 2022b</a>)"

image_content_right = make_image_block(**image_kwargs) 


slide_kwargs = deepcopy(dc_slide_kwargs)

slide_kwargs["content_str_0"] = image_content_left
slide_kwargs["content_str_1"] = image_content_right

slide_kwargs["header"] = "Self-organisation in glaberish CA"
slide_kwargs["after_fold"] = "" #after_fold_text # TODO image content for dw equations
slide_maker["function"] = make_double_column
slide_maker["slide_kwargs"] = slide_kwargs
slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)

# [ ] -deviation- bevodevo and pgens
image_kwargs = deepcopy(image_kwargs)
image_kwargs["image_filepath"] = "assets/nes_hopper42.png"
image_kwargs["link"] = "assets/nes_hopper42.png"
image_kwargs["image_alt_text"] = "HopperBulletEnv-v0 solution solved with natural evolution strategies () in bevodevo" 
image_kwargs["caption"] = ""
image_kwargs["image_width"] = 80

image_content_topleft = make_image_block(**image_kwargs) 

image_kwargs = deepcopy(image_kwargs)
image_kwargs["image_filepath"] = "assets/nes_hopper.gif"
image_kwargs["link"] = "assets/nes_hopper.gif"
image_kwargs["image_alt_text"] = "HopperBulletEnv-v0 solution solved with natural evolution strategies () in bevodevo" 
image_kwargs["caption"] = "HopperBulletEnv-v0 solution solved with natural evolution strategies (<a href='https://people.idsia.ch/~tom/publications/nes.pdf'>Wierstra <em>et al.</em> 2008</a>) in <a href='https://github.com/rivesunder/bevodevo'>bevodevo</a>: Bootstrapping Neep Neuroevolution and Developmental Learning"

image_content_bottomleft = make_image_block(**image_kwargs) 

image_kwargs = deepcopy(image_kwargs)
image_kwargs["image_filepath"] = "assets/swingup_fitness_landscape.png"
image_kwargs["link"] = "assets/swingup_fitness_landscape.png"
image_kwargs["image_alt_text"] = "A solution-generating landscape for InvertedPendulumSwingupBulletEnv-v0 using a simple Gaussian evo strategy" 
image_kwargs["caption"] = ""#A solution-generating landscape for InvertedPendulumBulletEnv-v0 using a simple Gaussian evo strategy"

image_content_topright = make_image_block(**image_kwargs) 

image_kwargs = deepcopy(image_kwargs)
image_kwargs["image_filepath"] = "assets/swingup_fitness_policies.gif"
image_kwargs["link"] = "assets/swingup_fitness_policies.gif"
image_kwargs["image_alt_text"] = "An evolved hopping glider(s) in an evolved CA rule s11 from the glaberish CA family" 
image_kwargs["caption"] = "Policies generated from latent (fitness landscape below) from an evolved policy-generating network evolved on the InvertedPendulumSwingupBulletEnv-v0 task"

image_content_bottomright = make_image_block(**image_kwargs) 

slide_kwargs = deepcopy(dc_slide_kwargs)

slide_kwargs["content_str_0"] = image_content_topleft +"<br><br>" +  image_content_bottomleft
slide_kwargs["content_str_1"] = image_content_bottomright + "<br><br>" + image_content_topright

slide_kwargs["header"] = "Evo-devo strategies in defined environments"
slide_kwargs["after_fold"] = "" #after_fold_text # TODO image content for dw equations
slide_maker["function"] = make_double_column
slide_maker["slide_kwargs"] = slide_kwargs
slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)

# [ ] CARLE and HARLI reflex glider
image_kwargs = deepcopy(image_kwargs)
image_kwargs["image_filepath"] = "assets/glider_reward.gif"
image_kwargs["link"] = "assets/glider_reward.gif"
image_kwargs["image_alt_text"] = "A glider (placed by the author) moving in CA RL environment that rewards changing center of mass" 
image_kwargs["caption"] = "A glider (placed by the author) moving in CA RL environment that rewards changing center of mass. The reflex glider, traveling at about c/4 (25% of maximum speed in Life) yields <strong>0.42 or 0.44 reward per step</strong>, and about 20 when crossing the edge of the action space or edge of the universe. From a cellular automata reinforcement learning environment project <a href='https://github.com/carle'>CARLE</a>/<a href='https://github.com/carles_game'>CARLE's game</a> (<a href='https://ieee-cog.org/2021/assets/papers/paper_329.pdf'>Davis 2021</a>)"

image_content = make_image_block(**image_kwargs) 

slide_kwargs = deepcopy(sc_slide_kwargs)
slide_kwargs["header"] = "A CA RL environment with a motility reward"
slide_kwargs["content_str"] = image_content
slide_kwargs["after_fold"] = "" #after_fold_text # TODO image content for dw equations
slide_maker["function"] = make_single_column
slide_maker["slide_kwargs"] = slide_kwargs
slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)

# [ ] CARLE and HARLI learning wave strategy
image_kwargs = deepcopy(image_kwargs)
image_kwargs["image_filepath"] = "assets/strategy_demo_127.gif"
image_kwargs["link"] = "assets/strategy_demo_127.gif"
image_kwargs["image_alt_text"] = "Hebbian Automata Reinforcement Learning Improviser (HARLI) demonstrates a wave strategy" 
image_kwargs["caption"] = "Hebbian Automata Reinforcement Learning Improviser (HARLI) demonstrates its 'wave' strategy. HARLI starts with randomly initialised weights and updates them according to an <span title='with covariance matrix evolution strategies'>evolved</span> Hebbian learning policy, eventually reaching a high-scoring wave generation strategy. The waves travel at c, the maximum speed in Life-like CA, and yield a reward of <span title='it uses a few other tricks to reach these scores'>about 40 to 50</span>. -> <a href='https://github.com/harli_learning'>https://github.com/rivesunder/harli_learning</a>, (<a href='https://ieee-cog.org/2021/assets/papers/paper_329.pdf'>Davis 2021</a>)"

image_content = make_image_block(**image_kwargs) 

slide_kwargs = deepcopy(sc_slide_kwargs)
slide_kwargs["header"] = "A Hebbian policy games a CA RL game"
slide_kwargs["content_str"] = image_content
slide_kwargs["after_fold"] = "" #after_fold_text # TODO image content for dw equations
slide_maker["function"] = make_single_column
slide_maker["slide_kwargs"] = slide_kwargs
slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)

# [ ] CARLE and HARLI learning generalizaiton (space ships don't work in all rulesets here)
image_kwargs = deepcopy(image_kwargs)
image_kwargs["image_filepath"] = "assets/spaceships.gif"
image_kwargs["link"] = "assets/spaceships.gif"
image_kwargs["image_width"] = 50
image_kwargs["image_alt_text"] = "HARLI's 'hack' was also more general over its training and evaluation tasks than a typical spaceship." 
image_kwargs["caption"] = "HARLI's hack was more general than typical spaceships as well. HARLI was evolved with rules B3/S023 (DotLife), B3/S236, B3/S237, B3/S238, and evaluated with Life itself (B3/S23). The lightweight spaceship (struggling above) only works in 2 of these rule sets, but the wave strategy <span title='HARLI also learned to take advantage of a _reset environment_ signal, which allowed it to score rewards higher than possible for c-speed motility'>works in all of them</span>."

image_content = make_image_block(**image_kwargs) 

slide_kwargs = deepcopy(sc_slide_kwargs)
slide_kwargs["header"] = "The Hebbian 'hack' was more general than constructing spaceships..."
slide_kwargs["content_str"] = image_content
slide_kwargs["after_fold"] = "" #after_fold_text # TODO image content for dw equations
slide_maker["function"] = make_single_column
slide_maker["slide_kwargs"] = slide_kwargs
slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)

# [ ] The Evolution will not be supervised

video_kwargs = deepcopy(image_kwargs)
video_kwargs.pop("image_filepath")
video_kwargs.pop("image_alt_text")
video_kwargs.pop("image_width")
video_kwargs["thumbnail_path"] = ""
video_kwargs["video_path"] = "assets/openended_s7_s11_s643_dt0.1_dt0.0100_dt0.1200_6.mp4"
video_kwargs["link"] = "assets/openended_s7_s11_s643_dt0.1_dt0.0100_dt0.1200_6.mp4"
video_kwargs["width"] = 640
video_kwargs["height"] = 640
video_kwargs["alt_text"] = "video of multichannel glaberish undergoing intrinsic evolution" 
video_kwargs["caption"] = "A multichannel CA universe seeded with gliders undergoes massive changes as gliders interact and adapt, combine, and eventually modify the environment to support a fluctuating background of rapidly replicating patterns"

video_content = make_video_block(**video_kwargs) 
my_video_kwargs = deepcopy(video_kwargs)

slide_kwargs = deepcopy(sc_slide_kwargs)
slide_kwargs["header"] = "The evolution will not be supervised"
slide_kwargs["content_str"] = video_content
slide_kwargs["after_fold"] = "" #after_fold_text # TODO image content for dw equations
slide_maker["function"] = make_single_column
slide_maker["slide_kwargs"] = slide_kwargs
slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)

# [ ] long trajectory RGB
image_kwargs = deepcopy(image_kwargs)
image_kwargs["image_filepath"] = "assets/tai_figure_rgb.png"
image_kwargs["link"] = "assets/tai_figure_rgb.png"
image_kwargs["image_width"] = 90
image_kwargs["image_alt_text"] = "A trajectory of intrinsic evolution in a multichannel CA" 
image_kwargs["caption"] = "A trajectory of the previous video. Maximum intensity projection with time on the horizontal axis"

image_content = make_image_block(**image_kwargs) 

slide_kwargs = deepcopy(sc_slide_kwargs)
slide_kwargs["header"] = "Intrinsic evo trajectory, time slice"
slide_kwargs["content_str"] = image_content
slide_kwargs["after_fold"] = "" #after_fold_text # TODO image content for dw equations
slide_maker["function"] = make_single_column
slide_maker["slide_kwargs"] = slide_kwargs
slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)

# [ ] long trajectory inverted
image_kwargs = deepcopy(image_kwargs)
image_kwargs["image_filepath"] = "assets/tai_figure_inverted.png"
image_kwargs["link"] = "assets/tai_figure_inverted.png"
image_kwargs["image_width"] = 90
image_kwargs["image_alt_text"] = "A trajectory of intrinsic evolution in a multichannel CA (inverted colormap)" 
image_kwargs["caption"] = "A trajectory of the previous video. Maximum intensity projection with time on the horizontal axis, inverted colours."

image_content = make_image_block(**image_kwargs) 

slide_kwargs = deepcopy(sc_slide_kwargs)
slide_kwargs["header"] = "Intrinsic evo trajectory, time slice (inverted)"
slide_kwargs["content_str"] = image_content
slide_kwargs["after_fold"] = "" #after_fold_text # TODO image content for dw equations
slide_maker["function"] = make_single_column
slide_maker["slide_kwargs"] = slide_kwargs
slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)

# [ ] long trajectory truncated
image_kwargs = deepcopy(image_kwargs)
image_kwargs["image_filepath"] = "assets/tai_figure_rgb_truncated.png"
image_kwargs["link"] = "assets/tai_figure_rgb_truncated.png"
image_kwargs["image_width"] = 90
image_kwargs["image_alt_text"] = "A trajectory of intrinsic evolution in a multichannel CA, truncated to show the rapid evo section" 
image_kwargs["caption"] = "A trajectory of the previous video, truncated to show the active replicative dynamics after the last phase change."

image_content = make_image_block(**image_kwargs) 

slide_kwargs = deepcopy(sc_slide_kwargs)
slide_kwargs["header"] = "Intrinsic evo trajectory, time slice (truncated)"
slide_kwargs["content_str"] = image_content
slide_kwargs["after_fold"] = "" #after_fold_text # TODO image content for dw equations
slide_maker["function"] = make_single_column
slide_maker["slide_kwargs"] = slide_kwargs
slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)

# [ ] long trajectory inverted truncated
image_kwargs = deepcopy(image_kwargs)
image_kwargs["image_filepath"] = "assets/tai_figure_inverted_truncated.png"
image_kwargs["link"] = "assets/tai_figure_inverted_truncated.png"
image_kwargs["image_width"] = 90
image_kwargs["image_alt_text"] = "A trajectory of intrinsic evolution in a multichannel CA, truncated to show the rapid evo section" 
image_kwargs["caption"] = "A trajectory of the previous video, truncated to show the active replicative dynamics after the last phase change (inverted colours)."

image_content = make_image_block(**image_kwargs) 

slide_kwargs = deepcopy(sc_slide_kwargs)
slide_kwargs["header"] = "Intrinsic evo trajectory, time slice (truncated, inverted)"
slide_kwargs["content_str"] = image_content
slide_kwargs["after_fold"] = "" #after_fold_text # TODO image content for dw equations
slide_maker["function"] = make_single_column
slide_maker["slide_kwargs"] = slide_kwargs
slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)

# [ ] open-endedness (some background, definitions, trivial oe, etc.)
points = []
points2 = []
points.append("Evo strategies are powerful, <strong>but</strong> vulnerable to specification gaming/reward hacking.")
points.append("I find intrinsic evolution (selection emerging in the same system that is subject to selection) a promising direction.")
points.append("Open-endedness has been broadly defined and often includes <strong>selection</strong> (<a href='https://dl.acm.org/doi/10.5555/2934046.2934113'>Maley 1999</a>), <strong>reproduction</strong> (<a href=''></a>, <a href='https://direct.mit.edu/isal/proceedings/alife2014/26/793/98965'>Soros+Stanley 2014</a>, <strong>increasing diversity</strong> (<a href='https://dl.acm.org/doi/10.5555/2934046.2934113'>Maley 1999</a>, ), <strong>increasing complexity</strong> (<a href='https://www.fullcircle.nexus/papers/taylor2015requirements.pdf'>Taylor 2015</a>, novelty/surprise (<a href='https://www.nature.com/articles/s41598-017-00810-8'>Adams <em>et al</em> 2017, <a href='https://www.fullcircle.nexus/papers/taylor2015requirements.pdf'>Taylor 2015</a>, <a href='https://direct.mit.edu/isal/proceedings/alife2014/26/793/98965'>Soros+Stanley 2014</a>), and <strong>adaptation</strong> (<a href='https://dl.acm.org/doi/10.5555/2934046.2934113'>Maley 1999</a>, )<span title='This is a non-comprehensive list with non-comprehensive citations'>.</span>")
points.append("(<a href='https://direct.mit.edu/artl/article/25/2/198/2923/Open-Endedness-for-the-Sake-of-Open-Endedness'>Hintze 2019</a>)demonstrated construction of a system that meets technical definitions of open-endedness while <strong>being rather boring</strong>.")
points.append("OE/OE evolution may be one of those '<strong>suitcase words</strong>', as M. Minsky <a href='https://en.wikipedia.org/wiki/The_Emotion_Machine' title='_e.g._ in _The Emotion Machine_ 2006'>would say</a>.") 


points2.append("<strong>Arend Hintze</strong>'s work used Levenshtein distance (sampled) and approximated Kolmogorov complexity with gzip compression. ")

text_content = make_text_block(bullet_points=points)
after_fold = make_text_block(bullet_points=points2)

slide_kwargs = deepcopy(sc_slide_kwargs)
slide_kwargs["after_fold"] = after_fold
slide_kwargs["content_str"] = text_content
slide_kwargs["header"] = "Intrinsic evolution and open-endedness"

slide_maker["function"] = make_single_column
slide_maker["slide_kwargs"] = slide_kwargs
slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)
# Existential forcing
# fnbeh-12-00330-g003.jpg
points = []
points2 = []
points.append("In Life, <strong>Conway</strong> was interested in a system that could vanish as well as grow.")
points.append("Does selection actually favor <span title='I think not. Selection is context dependent, but parsimony seems preferred'>limitlessly increasing complexity and growth?</span>")
points.append("Evolvability also evolves, and (as we can observe in cryptic phenotypes) past consistency is no guarantee of continued complacency.")
points.append("<span title='it is a bit of a tautology, but what is selected is selected'>'The universe gets what it selects for'.</span>")

text_content = make_text_block(bullet_points=points)


image_kwargs = deepcopy(image_kwargs)
image_kwargs["image_filepath"] = "assets/fnbeh-12-00330-g003.jpg"
image_kwargs["link"] = "assets/fnbeh-12-00330-g003.jpg"
image_kwargs["image_alt_text"] = "From Linda Weiss _Sensory Ecology of Predator-Induced Phenotypic Plasticity_ 2019 (CC BY)" 
image_kwargs["caption"] = "Cryptic phenotypes can be triggered by environmental conditions. Helmet expresison in <em>Daphnia</em> can be induced by presence of predators. From (<a href='https://www.frontiersin.org/journals/behavioral-neuroscience/articles/10.3389/fnbeh.2018.00330/full'>Weiss 2019</a>)."
image_kwargs["image_width"] = 100

image_content_left = make_image_block(**image_kwargs) 

slide_kwargs = deepcopy(dc_slide_kwargs)
slide_kwargs["content_str"] = text_content
slide_kwargs["header"] = "Cryptic phenotypes and parsimonious evolvability"
slide_kwargs.pop("content_str")
slide_kwargs["content_str_0"] = image_content_left
slide_kwargs["content_str_1"] = text_content
slide_kwargs["after_fold"] = "I am interested in <strong>integrating the concept of existential forcing found in DWs in systems capable of intrinsic evolution</strong>, or looking for intrinsic evolution in DaisyWorld-type models. <br><br> <strong>But</strong> we shouldn't lose sight of ethical considerations of building systems <a href='https://poets.org/poem/memoriam-h-h'>red in tooth in claw</a> that may contain entities capable of suffering (<em>e.g.</em> see <a href='https://gregegan.net/PERMUTATION/FAQ/FAQ.html'>Egan <~2007</a>, <a href='https://gregegan.net/MISC/CRYSTAL/Crystal.html'>Egan 2008</a>).<br><br>"

slide_maker["function"] = make_double_column
slide_maker["slide_kwargs"] = slide_kwargs
slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)
# [ ] Two paths
points = []
points2 = []
points.append("<strong>Two approaches</strong> to modeling characteristics of the exogenous forcing and intrinsic evolution of our own (LAWKI) experience.")
points.append("<strong> The emergence of self-organisation in DaisyWorlds</strong> (ESOiDW), or")
points.append("<strong>Incorporating DW-type forcing in self-organising systems</strong> capable of intrinsic evolution (DW to CA).")

text_content = make_text_block(bullet_points=points)
after_fold = make_text_block(bullet_points=points2)

slide_kwargs = deepcopy(sc_slide_kwargs)
slide_kwargs["after_fold"] = "" #after_fold
slide_kwargs["content_str"] = text_content
slide_kwargs["header"] = "Two paths"

slide_maker["function"] = make_single_column
slide_maker["slide_kwargs"] = slide_kwargs
slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)

# [ ] ESO in DWs
image_kwargs = deepcopy(image_kwargs)
image_kwargs["image_filepath"] = "assets/netlogo_dw_waves_light.gif"
image_kwargs["link"] = "assets/netlogo_dw_waves_light.gif"
image_kwargs["image_alt_text"] = "waves in a 2D DaisyWorld" 
image_kwargs["caption"] = "A 2D DaisyWorld implemented in NetLogo readily gives rise to waves. (<a href='https://ccl.northwestern.edu/netlogo/models/Daisyworld'>model</a> in <a href='https://www.netlogoweb.org/launch#http://ccl.northwestern.edu/netlogo/models/models/Sample%20Models/Biology/Daisyworld.nlogo'>NetLogo web</a>)"
image_kwargs["image_width"] = 100

image_content_left = make_image_block(**image_kwargs) 
# netlogo_dw_waves_light.webm
points = []
points2 = []
points.append("<- messy waves in NetLogo DaisyWorld")
points.append("Oscillations or wave-like dynamics observed in 0D (<a href='https://b.tellusjournals.se/articles/10.3402/tellusb.v51i4.16488'>Nevison <em>et al.</em> 1999</a>) and 2D (<a href='https://www.sciencedirect.com/science/article/abs/pii/S0022519306000786'>Wood <em>et al.</em> 2006</a>), stripe formation in a 1D DW (<a href='https://www.macs.hw.ac.uk/~awhite/adams_etal_jtb2003.pdf'>Adams <em>et al.</em>2003</a>)")
points.append("A differential equation DaisyWorld should be amenable to a <span title='_i.e._ the traveling wave solution'>'glider equation'</span> (<a href='https://arxiv.org/abs/2508.04167'>Kojima <em>et al.</em> 2025)")

text_content = make_text_block(bullet_points=points)
after_fold = make_text_block(bullet_points=points2)

slide_kwargs = deepcopy(dc_slide_kwargs)
slide_kwargs["after_fold"] = "" #after_fold

slide_kwargs["content_str_0"] = image_content_left
slide_kwargs["content_str_1"] = text_content
dc_slide_kwargs = deepcopy(slide_kwargs)

slide_kwargs["header"] = "Waves and oscillations in DaisyWorlds"
slide_maker["function"] = make_double_column

slide_maker["slide_kwargs"] = slide_kwargs
slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)

# [ ] Attempts at intrinsic OEE, e.g. in Flow-lenia

image_kwargs = deepcopy(image_kwargs)
image_kwargs["image_filepath"] = "assets/deserts_light_and_dark_000.gif"
image_kwargs["link"] = "assets/deserts_light_and_dark_000.gif"
image_kwargs["image_alt_text"] = "Desert formation in a 2D DaisyWorld" 
image_kwargs["caption"] = ""
image_kwargs["image_width"] = 70

image_content_left = make_image_block(**image_kwargs) 

points = []
points2 = []
points.append("Desert formation nucleates collapse in (<a href='https://www.sciencedirect.com/science/article/abs/pii/S0022519303000699'>Ackland <em>et al.</em> 2003</a>) and reviewed in (<a href='https://www.cell.com/trends/ecology-evolution/abstract/S0169-5347(03)00097-1'>Wilkinson <em>et al</em> 2003</a>).")
points.append("With the addition of mutation in (<a href='https://www.sciencedirect.com/science/article/abs/pii/S0022519306000786'>Wood <em>et al.</em> 2006</a>), 'cheating'>collapse is followed by recovery from refugia.")
points.append("Desert formation in a 2D DaisyWorld implemented by the author (<a href='https://github.com/rivesunder/therldaisyworld'>TheRLDaisyWorld</a>)")

text_content = make_text_block(bullet_points=points)
after_fold = make_text_block(bullet_points=points2)

slide_kwargs = deepcopy(sc_slide_kwargs)
slide_kwargs["after_fold"] = "" #after_fold

slide_kwargs["content_str"] = image_content_left + text_content

slide_kwargs["header"] = "Formation of deserts and refugia in DWs"
slide_maker["function"] = make_single_column

slide_maker["slide_kwargs"] = slide_kwargs
slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)
# [ ] Adding beta to glaberish (1/2)
image_kwargs = deepcopy(image_kwargs)
image_kwargs["image_filepath"] = "assets/big_glaberish_colored.jpg"
image_kwargs["link"] = "assets/big_glaberish_colored"
image_kwargs["image_width"] = 100
image_kwargs["image_alt_text"] = "Glaberish equation" 
image_kwargs["caption"] = ""

image_content = make_image_block(**image_kwargs) 

slide_kwargs = deepcopy(sc_slide_kwargs)
slide_kwargs["header"] = "Glaberish is a bivariate continuously valued CA."
slide_kwargs["content_str"] = image_content
slide_kwargs["after_fold"] = "" #after_fold_text # TODO image content for dw equations
slide_maker["function"] = make_single_column
slide_maker["slide_kwargs"] = slide_kwargs
slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)

# [ ] Adding beta to glaberish (1/2)
image_kwargs = deepcopy(image_kwargs)
image_kwargs["image_filepath"] = "assets/shorter_glaberish_colored_w_beta.jpg"
image_kwargs["link"] = "assets/big_glaberish_colored"
image_kwargs["image_width"] = 100
image_kwargs["image_alt_text"] = "glaberish CA equation with temperature dependence beta added" 
image_kwargs["caption"] = "Glaberish with a DaisyWorld temperature dependence (beta) added to modulated genesis function "

image_content = make_image_block(**image_kwargs) 

slide_kwargs = deepcopy(sc_slide_kwargs)
slide_kwargs["header"] = "Adding a DaisyWorld temperature dependence to glaberish"
slide_kwargs["content_str"] = image_content
slide_kwargs["after_fold"] = "" #after_fold_text # TODO image content for dw equations
slide_maker["function"] = make_single_column
slide_maker["slide_kwargs"] = slide_kwargs
slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)

# [ ]
#gliders_dw_glaberish6.mp4
video_kwargs = deepcopy(my_video_kwargs)

video_kwargs["thumbnail_path"] = ""
video_kwargs["video_path"] = "assets/dw_glaberish.mp4"
video_kwargs["link"] = "assets/dw_glaberish.mp4"
video_kwargs["width"] = 640
video_kwargs["height"] = 640
video_kwargs["alt_text"] = "video of multichannel glaberish undergoing intrinsic evolution, with temperature dependent genesis function" 
video_kwargs["caption"] = "Multichannel glaberish with temperature dependence and progressively increasing luminosity forcing. Each channel has a different albedo. "

video_content = make_video_block(**video_kwargs) 

slide_kwargs = deepcopy(sc_slide_kwargs)
slide_kwargs["header"] = "DaisyWorld + glaberish"
slide_kwargs["content_str"] = video_content
slide_kwargs["after_fold"] = "" #after_fold_text # TODO image content for dw equations
slide_maker["function"] = make_single_column
slide_maker["slide_kwargs"] = slide_kwargs
slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)

#gliders_dw_glaberish6.mp4
video_kwargs = deepcopy(my_video_kwargs)

video_kwargs["thumbnail_path"] = ""
video_kwargs["video_path"] = "assets/ndw_glaberish.mp4"
video_kwargs["link"] = "assets/ndw_glaberish.mp4"
video_kwargs["width"] = 640
video_kwargs["height"] = 640
video_kwargs["alt_text"] = "video of multichannel glaberish undergoing intrinsic evolution, with temperature dependent genesis function, neutral albedo activations" 
video_kwargs["caption"] = "Multichannel glaberish with temperature dependence and progressively increasing luminosity forcing. Each channel has the same albedo as background."

video_content = make_video_block(**video_kwargs) 

slide_kwargs = deepcopy(sc_slide_kwargs)
slide_kwargs["header"] = "DaisyWorld + glaberish (neutral albedo)"
slide_kwargs["content_str"] = video_content
slide_kwargs["after_fold"] = "" #after_fold_text # TODO image content for dw equations
slide_maker["function"] = make_single_column
slide_maker["slide_kwargs"] = slide_kwargs
slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)

# [ ] Attempts at intrinsic OEE, e.g. in multichannel CA
image_kwargs = deepcopy(image_kwargs)
image_kwargs["image_filepath"] = "assets/planetary_boundaries_2023.png"
image_kwargs["link"] = "assets/planetary_boundaries_2023.png"
image_kwargs["image_alt_text"] = "Planetary boundaries diagram from Stockholm Resilience Centre" 
image_kwargs["caption"] = "CC BY-NC-ND 3.0 Azote for <a href='https://www.stockholmresilience.org/research/planetary-boundaries.html'>Stockholm Resilience Centre</a>, based on analysis in Richardson et al 2023"
image_kwargs["image_width"] = 100

image_content_left = make_image_block(**image_kwargs) 

points = []
points2 = []
points.append("Informing the <strong>search for extra-terrestrial life</strong> by considering implied goals in service to habitability.")
points.append("Would driving a complex system with a trivially infinite/OE-adjacent process yield interesting <strong>intrinsic evo or OE</strong>?")
points.append("Would self-organisation arise at certain points in a forcing trajectory (and how might this affect persistence), informing thinking about <strong>origins of life</strong>.")
points.append("Building abstract understanding of <strong>planetary boundaries</strong> (<em>e.g.</em> <a href='https://www.science.org/doi/10.1126/sciadv.adh2458'>Richardson <em>et al.</em></a> 2023), and exoplanetary habitability with biogenic feedback.")

text_content = make_text_block(bullet_points=points)
after_fold = make_text_block(bullet_points=points2)

slide_kwargs = deepcopy(dc_slide_kwargs)
slide_kwargs["after_fold"] = "" #after_fold

slide_kwargs["content_str_0"] = image_content_left
slide_kwargs["content_str_1"] = text_content
dc_slide_kwargs = deepcopy(slide_kwargs)

slide_kwargs["header"] = "Why(selection, self-organisation, and planetary homeostasis)."
slide_maker["function"] = make_double_column

slide_maker["slide_kwargs"] = slide_kwargs
slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)

# [ ] Solitons, evo vs. analytical (where should this slide go ???)
# [ ] Questions slide, contact info, references

# slides with extra notes/question answers?
image_kwargs = deepcopy(image_kwargs)
# crosslabs logo
#<!-- https://cdn.prod.website-files.com/5e13ec90eb497caec7970be9/62709f41991bfb59f68a770a_webclip-256x256.png -->
# https://static.wixstatic.com/media/5d827c_77afe4e51fa74d7d8e4cae23a235540d~mv2.png/v1/crop/x_0,y_17,w_201,h_87/fill/w_154,h_64,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/rogo.png
#image_kwargs["image_filepath"] = "https://cdn.prod.website-files.com/5e13ec90eb497caec7970be9/63f01ef004f1d7a6c817909d_Open%20Graph%201200x630.png"
video_kwargs = deepcopy(my_video_kwargs)

video_kwargs["thumbnail_path"] = ""
video_kwargs["video_path"] = "assets/gliders1.mp4"
video_kwargs["link"] = "assets/gliders1.mp4"
video_kwargs["width"] = 640
video_kwargs["height"] = 640
video_kwargs["alt_text"] = "video of multichannel glaberish undergoing intrinsic evolution, with temperature dependent genesis function, neutral albedo activations" 
video_kwargs["caption"] = ""

video_content = make_video_block(**video_kwargs) 

image_kwargs["image_filepath"] = "https://cdn.prod.website-files.com/5e13ec90eb497caec7970be9/62709f41991bfb59f68a770a_webclip-256x256.png "
image_kwargs["link"] = "https://www.crosslabs.org/"
image_kwargs["image_alt_text"] = "" 
image_kwargs["image_width"] = 15
image_kwargs["caption"] = ""

image_content_one = make_image_block(**image_kwargs) 

image_kwargs = deepcopy(image_kwargs)
image_kwargs["image_filepath"] = "https://static.wixstatic.com/media/5d827c_77afe4e51fa74d7d8e4cae23a235540d~mv2.png"
image_kwargs["link"] = "https://www.cross-compass.com"
image_kwargs["image_alt_text"] = "" 
image_kwargs["image_width"] = 50
image_kwargs["caption"] = "" #Supported by <a href='https://www.crosslabs.org'>Cross Labs</a> and <a href='https://www.cross-compass.com'>Cross Compass</a>."

image_content_two = make_image_block(**image_kwargs) 

slide_kwargs = deepcopy(sc_slide_kwargs)
slide_kwargs["content_str"] = "Supported by <a href='https://www.crosslabs.org'>Cross Labs</a> and <a href='https://www.cross-compass.com'>Cross Compass</a>.<br><br>" + image_content_one + image_content_two + video_content
slide_kwargs["after_fold"] = ""

slide_kwargs["header"] = "Thanks (time for Qs)"
slide_kwargs["caption"] = ""
slide_maker["function"] = make_single_column
slide_maker["slide_kwargs"] = slide_kwargs

slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)

video_kwargs = deepcopy(my_video_kwargs)

video_kwargs["thumbnail_path"] = ""
video_kwargs["video_path"] = "assets/ngliders1.mp4"
video_kwargs["link"] = "assets/ngliders1.mp4"
video_kwargs["width"] = 640
video_kwargs["height"] = 640
video_kwargs["alt_text"] = "" 
video_kwargs["caption"] = ""

video_content = make_video_block(**video_kwargs) 

image_kwargs["image_filepath"] = "https://cdn.prod.website-files.com/5e13ec90eb497caec7970be9/62709f41991bfb59f68a770a_webclip-256x256.png "
image_kwargs["link"] = "https://www.crosslabs.org/"
image_kwargs["image_alt_text"] = "" 
image_kwargs["image_width"] = 15
image_kwargs["caption"] = ""

image_content_one = make_image_block(**image_kwargs) 

image_kwargs = deepcopy(image_kwargs)
image_kwargs["image_filepath"] = "https://static.wixstatic.com/media/5d827c_77afe4e51fa74d7d8e4cae23a235540d~mv2.png"
image_kwargs["link"] = "https://www.cross-compass.com"
image_kwargs["image_alt_text"] = "" 
image_kwargs["image_width"] = 50
image_kwargs["caption"] = "" #Supported by <a href='https://www.crosslabs.org'>Cross Labs</a> and <a href='https://www.cross-compass.com'>Cross Compass</a>."

image_content_two = make_image_block(**image_kwargs) 

slide_kwargs = deepcopy(sc_slide_kwargs)
slide_kwargs["content_str"] = "Supported by <a href='https://www.crosslabs.org'>Cross Labs</a> and <a href='https://www.cross-compass.com'>Cross Compass</a>.<br><br>" + image_content_one + image_content_two + video_content
slide_kwargs["after_fold"] = ""

slide_kwargs["header"] = "Thanks (time for Qs)"
slide_kwargs["caption"] = ""
slide_maker["function"] = make_single_column
slide_maker["slide_kwargs"] = slide_kwargs

slide_makers, slides, slide_index = update_slides_list(slide_makers, \
    slide_maker, slides, slide_index)

# build the slide deck!
for mk_idx, slide_mkr in enumerate(slide_makers):

  slide_mkr["slide_kwargs"]["slides"] = slides
  slide_mkr["slide_kwargs"]["slide_idx"] = mk_idx

  html = slide_mkr["function"](**slide_mkr["slide_kwargs"])

  with open(slides[mk_idx], "w") as f:
    f.write(html)
