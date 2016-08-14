using UnityEngine;
using System.Collections;

public class Planet : MonoBehaviour
{
	public Sprite[] sprites;
	private Animator animator;
	private int healthVal;
	private bool damaged;
	private SpriteRenderer planetSprite;
	void Awake()
	{
		planetSprite = GetComponentInChildren<SpriteRenderer>();
		int randomize = Random.Range(0, sprites.Length);
		planetSprite.sprite = sprites[randomize];
	}
	void Start()
	{
		animator = GetComponent<Animator>();


	}

	void OnTriggerStay2D(Collider2D collider)
	{
		Attacker attacker = collider.gameObject.GetComponent<Attacker>();
		Animator attackAnim = collider.gameObject.GetComponent<Animator>();
		//We only want to trigger the animation when the attacker is attacking
		if (attacker && attackAnim.GetBool("isAttacking"))
		{
			animator.SetTrigger("underAttack");
		}
	}
}
