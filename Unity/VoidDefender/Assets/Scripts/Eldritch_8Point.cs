using UnityEngine;
using System.Collections;
[RequireComponent(typeof(Attacker))] //protection to ensure that we have an Attacker. Will add Attacker if there isn't one
public class Eldritch_8Point : MonoBehaviour
{

	// Use this for initialization
	private Attacker attacker;
	private Animator anim;
	private bool notTired;
	private Health health;

	void Start()
	{
		notTired = true;
		attacker = gameObject.GetComponent<Attacker>();
		anim = gameObject.GetComponent<Animator>();
		health = gameObject.GetComponent<Health>();
		health.SetSealImmune(true);
	}

	void OnTriggerStay2D(Collider2D col)
	{
		GameObject obj = col.gameObject;
		if (!obj.GetComponent<Defender>())
		{
			//abort if not colliding with Defender
			return;
		}
		/*print(obj);
		if (obj.GetComponent<Monolith>())
		{
			print("I'm dealing with a Monolith");
		}*/
		if (obj.GetComponent<Eldritch_Seal>()  && health.GetSealImmune())
		{
			//Eldritch Seals can kill when placed on top, unlike Monoliths which cannot impede if behind
			//animate when the character can warp
			anim.SetTrigger("warpTrigger");
			notTired = false;

		}
		else if (transform.position.x < col.transform.position.x)
		{
			return;//Just keep going
		}
		else if (obj.GetComponent<Monolith>() && health.GetSealImmune())
		{
			//only skip the monolith if we're in front of it
			//animate when the character can warp
			anim.SetTrigger("warpTrigger");
			notTired = false;

		}
		else {

			anim.SetBool("isAttacking", true);
			attacker.Attack(obj);
		}
	}

}
