using UnityEngine;
using System.Collections;

public class Eldritch_Seal : MonoBehaviour {

	// Use this for initialization

	private Animator animator;
	private bool hasExploded = false;

	public int damage=6;
	void Start()
	{
		animator = GetComponent<Animator>();

	}

	void OnTriggerStay2D(Collider2D collider)
	{
		if (hasExploded)
		{
			//skip if we have explode
			return;
		}
		Attacker attacker = collider.gameObject.GetComponent<Attacker>();
		Health health = collider.gameObject.GetComponent<Health>();
		
		if (!health || health.GetSealImmune())//skip if we health doesn't exist, or it's immune
		{
			return;
		}
		
		if (attacker)
		{
			hasExploded = true;
			health.DealDamage(damage);//explodes. A maxed out White Spawn on the hardest difficulty should be able to survive
			gameObject.GetComponent<Health>().DestroyObject();//kills self
		}

	}
}
