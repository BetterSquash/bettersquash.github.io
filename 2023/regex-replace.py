import os
import re

def replace_in_file(file_path, replacements):
    with open(file_path, 'r') as file:
        content = file.read()
    
    for find_text, replace_text in replacements.items():
        # Compile the regex pattern with DOTALL flag
        pattern = re.compile(find_text, re.DOTALL)
        # Perform the replacement
        content = pattern.sub(replace_text, content)
    
    with open(file_path, 'w') as file:
        file.write(content)

def process_files_in_folder(replacements):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    for file_name in os.listdir(current_directory):
        if file_name.endswith('.html'):
            file_path = os.path.join(current_directory, file_name)
            replace_in_file(file_path, replacements)

def main():
    replacements = {
        r'<!--Video Analysis Ad Start-->.*?<!--Video Analysis Ad End-->': '',
        r'<h3 class="f2 lh-solid sans-serif">Watch.*?</body>': 'FOOTERHERE',
        r'FOOTERHERE': '<p><a href="#top">BACK TO TOP ↑</a></p>\n<hr class="content"/>\n<footer>\n<!--Tagline-->\n<h3>Mantra</h3>\n<p class="mantra tcolor">Do something every single day to improve your squash!</p>\n<hr class="footerdivider"/>\n<!--SRM-->\n<h3>Improve Your Solo Practice</h3>\n<p>Get a <a href="/srm/">monthly solo routine</a> sent to you by email.</p>\n<hr class="footerdivider"/>\n<!--Random-->\n<h3>Feeling Lucky?</h3>\n<p>Read a <a href="/random.html" id="RandomLink" onclick="RandomArticle();return false;" title="Read a random article">Random Article</a> or watch a <a href="/random.html" id="RandomVideo" onclick="RandomVideo();return false;" title="Watch a random video">Random Video</a>.</p>\n<hr class="footerdivider"/>\n<!--Video-->\n<h3>Watch This To Improve Your Squash</h3>\n<lite-youtube loading="lazy" params="rel=0" playlabel="Watch This Video To Improve Your Squash" videoid="C-dxMogZLDM"></lite-youtube>\n<hr class="footerdivider"/>\n<!--About Me-->\n<h3>About Me</h3>\n<p>I am a squash coach with nearly 40 years experience; teaching complete beginners through to professionals.<br/>Currently, I call myself an "online squash coach" as I rarely coach on court.<br/>I enjoy working with club players and strive to present information in an entertaining and engaging way.</p>\n<hr class="footerdivider"/>\n<!--Social Media-->\n<h3>Social Media</h3>\n<p>Follow me on <a href="https://www.youtube.com/@BetterSquash/community" title="Follow me on YouTube Community">YouTube Community</a>, <a href="https://www.instagram.com/bettersquash/" title="Follow me on Instagram">Instagram</a>, <a href="https://www.threads.net/@bettersquash" title="Follow me on Threads">Threads</a>, <a href="https://www.reddit.com/user/SquashCoachPhillip/" title="Follow me on Reddit">Reddit</a> and <a href="https://www.linkedin.com/in/phillip-marlowe/" title="Follow me on LinkedIn">LinkedIn</a>.</p>\n<hr class="footerdivider tcolor"/>\n<!--Gallery-->\n<h3>Vintage Squash Gallery</h3>\n<p>Visit the <a href="/gallery.html">Gallery</a> for images of vintage squash equipment, players, courts, balls and more.</p>\n<hr class="footerdivider"/>\n<!--SquashTV-->\n<h3>20&#37; SquashTV Discount</h3>\n<p>Receive a 20&#37; Squash TV subscription discount by using this link: <a href="https://lddy.no/1j4np">https://lddy.no/1j4np</a>.  Then enter this code: "<em>BETTERSQUASH20</em>"</p>\n<hr class="footerdivider"/>\n<!--Video Analysis-->\n<h3>Video Analysis</h3>\n<p>Send me a recording of you playing a competitive match and I do a "<em>live recording analysis</em>". I give you easy-to-understand, actionable points to help you improve. Full details on the <a href="/va/">Video Analysis</a> page.</p>\n<hr class="footerdivider"/>\n<!--Images Credit-->\nMORETOFOLLOW',
         r'MORETOFOLLOW': '<h3>Images Credit</h3>\n<p>All the images on this page, including the Open Graph image, are courtesy of <a href="https://www.instagram.com/rpzil/">Petteri Repo</a><sup><svg height="8px" id="Layer_1" version="1.1" viewbox="0 0 551.034 551.034" width="8px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><g id="XMLID_13_"><lineargradient gradienttransform="matrix(1 0 0 -1 0 554)" gradientunits="userSpaceOnUse" id="XMLID_2_" x1="275.517" x2="275.517" y1="4.5714" y2="549.7202"><stop offset="0" style="stop-color:#E09B3D"></stop><stop offset="0.3" style="stop-color:#C74C4D"></stop><stop offset="0.6" style="stop-color:#C21975"></stop><stop offset="1" style="stop-color:#7024C4"></stop></lineargradient><path d="M386.878,0H164.156C73.64,0,0,73.64,0,164.156v222.722c0,90.516,73.64,164.156,164.156,164.156h222.722c90.516,0,164.156-73.64,164.156-164.156V164.156C551.033,73.64,477.393,0,386.878,0z M495.6,386.878c0,60.045-48.677,108.722-108.722,108.722H164.156c-60.045,0-108.722-48.677-108.722-108.722V164.156c0-60.046,48.677-108.722,108.722-108.722h222.722c60.045,0,108.722,48.676,108.722,108.722L495.6,386.878L495.6,386.878z" id="XMLID_17_" style="fill:url(#XMLID_2_);"></path><lineargradient gradienttransform="matrix(1 0 0 -1 0 554)" gradientunits="userSpaceOnUse" id="XMLID_3_" x1="275.517" x2="275.517" y1="4.5714" y2="549.7202"><stop offset="0" style="stop-color:#E09B3D"></stop><stop offset="0.3" style="stop-color:#C74C4D"></stop><stop offset="0.6" style="stop-color:#C21975"></stop><stop offset="1" style="stop-color:#7024C4"></stop></lineargradient><path d="M275.517,133C196.933,133,133,196.933,133,275.516s63.933,142.517,142.517,142.517S418.034,354.1,418.034,275.516S354.101,133,275.517,133z M275.517,362.6c-48.095,0-87.083-38.988-87.083-87.083s38.989-87.083,87.083-87.083c48.095,0,87.083,38.988,87.083,87.083C362.6,323.611,323.611,362.6,275.517,362.6z" id="XMLID_81_" style="fill:url(#XMLID_3_);"></path><lineargradient gradienttransform="matrix(1 0 0 -1 0 554)" gradientunits="userSpaceOnUse" id="XMLID_4_" x1="418.306" x2="418.306" y1="4.5714" y2="549.7202"><stop offset="0" style="stop-color:#E09B3D"></stop><stop offset="0.3" style="stop-color:#C74C4D"></stop><stop offset="0.6" style="stop-color:#C21975"></stop><stop offset="1" style="stop-color:#7024C4"></stop></lineargradient><circle cx="418.306" cy="134.072" id="XMLID_83_" r="34.149" style="fill:url(#XMLID_4_);"></circle></g></svg></sup> and displayed using the AVIF format.</p>\n<hr class="footerdivider"/>\nEVENMORETOFOLLOW',
         r'EVENMORETOFOLLOW': '<!--NO COOKIES-->\n<h3>No Cookies or Advertising</h3>\n<p>BetterSquash.com does not contain any tracking code nor advertisements.</p>\n<hr class="footerdivider"/>\n<!--RSS Feed-->\n<h3>RSS Feed</h3>\n<p>Subscribe to the <a href="/bettersquash_feed.xml">RSS/Atom</a><sup><?xml version="1.0" encoding="UTF-8" standalone="no"?><svg height="8px" version="1.1" viewbox="0 0 44 44" width="8px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><title>BetterSquash RSS Feed</title><desc>Get Updates Delivered To Your Reader</desc><defs></defs> <g fill="none" fill-rule="evenodd" id="Icons" stroke="none" stroke-width="1"><g fill="#FF9A00" id="Color-" transform="translate(-800.000000, -760.000000)"><path d="M800.000471,797.714286 C800.000471,794.243 802.81487,791.428571 806.286118,791.428571 C809.757367,791.428571 812.571765,794.243 812.571765,797.714286 C812.571765,801.185571 809.757367,804 806.286118,804 C802.81487,804 800.000471,801.185571 800.000471,797.714286 Z M844,804 L835.619661,804 C835.619661,784.358714 819.641547,768.380429 800.000471,768.380429 L800.000471,760 C824.261497,760 844,779.738714 844,804 Z M829.333543,804 L820.953204,804 C820.953204,792.446857 811.553019,783.048143 800,783.048143 L800,774.666143 C816.174541,774.666143 829.333543,787.825286 829.333543,804 Z" id="RSS"></path></g></g></svg></sup> feed.MOREMOREMORE',
          r'MOREMOREMORE': '</p>\n<hr class="footerdivider"/>\n<!--Footer-->\n<p class="footerp">© 2024 Phillip Marlowe - phillip@bettersquash.com</p>\n<p><a href="#top">BACK TO TOP ↑</a></p>\n</footer></body>',
          r'<h2>Watch.*?</body>': 'FOOTERHERE',
          r'FOOTERHERE': '<p><a href="#top">BACK TO TOP ↑</a></p>\n<hr class="content"/>\n<footer>\n<!--Tagline-->\n<h3>Mantra</h3>\n<p class="mantra tcolor">Do something every single day to improve your squash!</p>\n<hr class="footerdivider"/>\n<!--SRM-->\n<h3>Improve Your Solo Practice</h3>\n<p>Get a <a href="/srm/">monthly solo routine</a> sent to you by email.</p>\n<hr class="footerdivider"/>\n<!--Random-->\n<h3>Feeling Lucky?</h3>\n<p>Read a <a href="/random.html" id="RandomLink" onclick="RandomArticle();return false;" title="Read a random article">Random Article</a> or watch a <a href="/random.html" id="RandomVideo" onclick="RandomVideo();return false;" title="Watch a random video">Random Video</a>.</p>\n<hr class="footerdivider"/>\n<!--Video-->\n<h3>Watch This To Improve Your Squash</h3>\n<lite-youtube loading="lazy" params="rel=0" playlabel="Watch This Video To Improve Your Squash" videoid="C-dxMogZLDM"></lite-youtube>\n<hr class="footerdivider"/>\n<!--About Me-->\n<h3>About Me</h3>\n<p>I am a squash coach with nearly 40 years experience; teaching complete beginners through to professionals.<br/>Currently, I call myself an "online squash coach" as I rarely coach on court.<br/>I enjoy working with club players and strive to present information in an entertaining and engaging way.</p>\n<hr class="footerdivider"/>\n<!--Social Media-->\n<h3>Social Media</h3>\n<p>Follow me on <a href="https://www.youtube.com/@BetterSquash/community" title="Follow me on YouTube Community">YouTube Community</a>, <a href="https://www.instagram.com/bettersquash/" title="Follow me on Instagram">Instagram</a>, <a href="https://www.threads.net/@bettersquash" title="Follow me on Threads">Threads</a>, <a href="https://www.reddit.com/user/SquashCoachPhillip/" title="Follow me on Reddit">Reddit</a> and <a href="https://www.linkedin.com/in/phillip-marlowe/" title="Follow me on LinkedIn">LinkedIn</a>.</p>\n<hr class="footerdivider tcolor"/>\n<!--Gallery-->\n<h3>Vintage Squash Gallery</h3>\n<p>Visit the <a href="/gallery.html">Gallery</a> for images of vintage squash equipment, players, courts, balls and more.</p>\n<hr class="footerdivider"/>\n<!--SquashTV-->\n<h3>20&#37; SquashTV Discount</h3>\n<p>Receive a 20&#37; Squash TV subscription discount by using this link: <a href="https://lddy.no/1j4np">https://lddy.no/1j4np</a>.  Then enter this code: "<em>BETTERSQUASH20</em>"</p>\n<hr class="footerdivider"/>\n<!--Video Analysis-->\n<h3>Video Analysis</h3>\n<p>Send me a recording of you playing a competitive match and I do a "<em>live recording analysis</em>". I give you easy-to-understand, actionable points to help you improve. Full details on the <a href="/va/">Video Analysis</a> page.</p>\n<hr class="footerdivider"/>\n<!--Images Credit-->\nMORETOFOLLOW',
           r'MORETOFOLLOW': '<h3>Images Credit</h3>\n<p>All the images on this page, including the Open Graph image, are courtesy of <a href="https://www.instagram.com/rpzil/">Petteri Repo</a><sup><svg height="8px" id="Layer_1" version="1.1" viewbox="0 0 551.034 551.034" width="8px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><g id="XMLID_13_"><lineargradient gradienttransform="matrix(1 0 0 -1 0 554)" gradientunits="userSpaceOnUse" id="XMLID_2_" x1="275.517" x2="275.517" y1="4.5714" y2="549.7202"><stop offset="0" style="stop-color:#E09B3D"></stop><stop offset="0.3" style="stop-color:#C74C4D"></stop><stop offset="0.6" style="stop-color:#C21975"></stop><stop offset="1" style="stop-color:#7024C4"></stop></lineargradient><path d="M386.878,0H164.156C73.64,0,0,73.64,0,164.156v222.722c0,90.516,73.64,164.156,164.156,164.156h222.722c90.516,0,164.156-73.64,164.156-164.156V164.156C551.033,73.64,477.393,0,386.878,0z M495.6,386.878c0,60.045-48.677,108.722-108.722,108.722H164.156c-60.045,0-108.722-48.677-108.722-108.722V164.156c0-60.046,48.677-108.722,108.722-108.722h222.722c60.045,0,108.722,48.676,108.722,108.722L495.6,386.878L495.6,386.878z" id="XMLID_17_" style="fill:url(#XMLID_2_);"></path><lineargradient gradienttransform="matrix(1 0 0 -1 0 554)" gradientunits="userSpaceOnUse" id="XMLID_3_" x1="275.517" x2="275.517" y1="4.5714" y2="549.7202"><stop offset="0" style="stop-color:#E09B3D"></stop><stop offset="0.3" style="stop-color:#C74C4D"></stop><stop offset="0.6" style="stop-color:#C21975"></stop><stop offset="1" style="stop-color:#7024C4"></stop></lineargradient><path d="M275.517,133C196.933,133,133,196.933,133,275.516s63.933,142.517,142.517,142.517S418.034,354.1,418.034,275.516S354.101,133,275.517,133z M275.517,362.6c-48.095,0-87.083-38.988-87.083-87.083s38.989-87.083,87.083-87.083c48.095,0,87.083,38.988,87.083,87.083C362.6,323.611,323.611,362.6,275.517,362.6z" id="XMLID_81_" style="fill:url(#XMLID_3_);"></path><lineargradient gradienttransform="matrix(1 0 0 -1 0 554)" gradientunits="userSpaceOnUse" id="XMLID_4_" x1="418.306" x2="418.306" y1="4.5714" y2="549.7202"><stop offset="0" style="stop-color:#E09B3D"></stop><stop offset="0.3" style="stop-color:#C74C4D"></stop><stop offset="0.6" style="stop-color:#C21975"></stop><stop offset="1" style="stop-color:#7024C4"></stop></lineargradient><circle cx="418.306" cy="134.072" id="XMLID_83_" r="34.149" style="fill:url(#XMLID_4_);"></circle></g></svg></sup> and displayed using the AVIF format.</p>\n<hr class="footerdivider"/>\nEVENMORETOFOLLOW',
           r'EVENMORETOFOLLOW': '<!--NO COOKIES-->\n<h3>No Cookies or Advertising</h3>\n<p>BetterSquash.com does not contain any tracking code nor advertisements.</p>\n<hr class="footerdivider"/>\n<!--RSS Feed-->\n<h3>RSS Feed</h3>\n<p>Subscribe to the <a href="/bettersquash_feed.xml">RSS/Atom</a><sup><?xml version="1.0" encoding="UTF-8" standalone="no"?><svg height="8px" version="1.1" viewbox="0 0 44 44" width="8px" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><title>BetterSquash RSS Feed</title><desc>Get Updates Delivered To Your Reader</desc><defs></defs> <g fill="none" fill-rule="evenodd" id="Icons" stroke="none" stroke-width="1"><g fill="#FF9A00" id="Color-" transform="translate(-800.000000, -760.000000)"><path d="M800.000471,797.714286 C800.000471,794.243 802.81487,791.428571 806.286118,791.428571 C809.757367,791.428571 812.571765,794.243 812.571765,797.714286 C812.571765,801.185571 809.757367,804 806.286118,804 C802.81487,804 800.000471,801.185571 800.000471,797.714286 Z M844,804 L835.619661,804 C835.619661,784.358714 819.641547,768.380429 800.000471,768.380429 L800.000471,760 C824.261497,760 844,779.738714 844,804 Z M829.333543,804 L820.953204,804 C820.953204,792.446857 811.553019,783.048143 800,783.048143 L800,774.666143 C816.174541,774.666143 829.333543,787.825286 829.333543,804 Z" id="RSS"></path></g></g></svg></sup> feed.MOREMOREMORE',
            r'MOREMOREMORE': '</p>\n<hr class="footerdivider"/>\n<!--Footer-->\n<p class="footerp">© 2024 Phillip Marlowe - phillip@bettersquash.com</p>\n<p><a href="#top">BACK TO TOP ↑</a></p>\n</footer></body>',
        
         # No DOTALL flag here
        # Add more replacements as needed
    }
    process_files_in_folder(replacements)

if __name__ == "__main__":
    main()
