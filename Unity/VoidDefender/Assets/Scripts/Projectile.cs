using UnityEngine;
using System.Collections;

public class Projectile : MonoBehaviour {

	public float speed, damage;
	private bool hasHit;
	// Use this for initialization
	void Start () {
		hasHit = false;
	}
	
	// Update is called once per frame
	void Update () {
		transform.Translate(Vector3.right * speed * Time.deltaTime);
	
	}

	void OnTriggerEnter2D (Collider2D collider)
	{
		Attacker attacker = collider.gameObject.GetComponent<Attacker>();
		if (!attacker)
		{
			//skips things if the object is not an attacker
			return;
		}
		Health health = collider.gameObject.GetComponent<Health>();
		if (attacker && health && !hasHit)
		{
			//make sure this only gets invoked once
			hasHit = true;
			health.DealDamage(damage);
			Destroy(gameObject);//destroy self
		}

	}
}
