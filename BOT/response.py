from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("מי","שלום","היי","מה נשמה"):
        return "Salut ! Comment ca va 💞? "

    if user_message in ("מי אתה?","מי זה?", "מי זה", "עם מי אני מדברת"):
        return " C'est moi sasha, ton mari 🖤❤️"
    
    if user_message in ("מי אני אוהבת?","אוהבת אותך","אני אוהבת אותך"):
        return "Je t'aime aussi mon coeur ❤️❤️❤️"

    if user_message in ("מאמי?","שרי?","סשה?","סשה"):
        return "Oui cherie 💖 ? "

    if user_message in ("מה אתה עושה?","מה אתה עושה","מה עושה?","מה עושה"):
        return "Je parle avec toi mdrrrr !"
    
    if user_message in ("לא טוב","נו","אוקי","אני לא מרגישה טוב"):
        return "Qu'est ce qu'il se passe mon amour ??"

    if user_message in ("אתה אוהב אותי?"):
        return "Je t'aime plus que tout au monde ma princesse❤️🖤💜💓💞"

    if user_message in ("משעמם","אוףף","משעמם לי"):
        return "Mdrr oui je sais tkt, qu'est ce tu veux que je fasse ?"

    if user_message in ("אני עייפה"):
        return "Ah bon ? Mdrrr tkt tu vas dormir ce soir, avec moi😏"

    if user_message in ("אין לי כוח"):
        return "Mais si tkt tu vas en avoir, ai confiance en toi tout vas bien se passer cherie❤️"

    if user_message in ("כואב לי הראש"):
        return "Ah merde, t'as pris un doliprane ? C'est a cause d'un connard au telephone ?mdrrr"
    
    if user_message in ("נימאס לי אוףף"):
        return "Quoi ? Pq, c'est quoi le probleme ?? "

    if user_message in ("בא לי אותך"):
        return "Moi aussi ma coquine, tres tres envie de toi😏😏🖕🍑🍆"

    if user_message in ("קשה לייי"):
        return "Je sais mon coeur, tkt je suis la moi 🤗"

    if user_message in ("למה לא עונה"):
        return "C'est impossible je te repond toujours mdrrrrrr😂😂"

    if user_message in ("אני צריכה חיזוק"):
        return "Cherie tkt pas pour tous tes problemes. N'oublies jamais que c'est pas toi marlite les choses. Tout vas bien se passer fais moi confiance, ai confiance en Dieu, ya que lui qui va t'aider. Ne pers jamais la emouna que c'est lui qui controle tout, pas toi, ni moi. Ne t'inquite de rien surtout, rien n'est important. Tu me fais confiance ma princesse ? 💖"

    if user_message in ("כן"):
        return "Super mon bébé !"
    
    if user_message in ("לא"):
        return "Pourquoi non ?🥺"



    return "J'ai pas compris cheri, ecris le bien ! Si tu veux me poser une question n'oublie pas le ? apres le mot"